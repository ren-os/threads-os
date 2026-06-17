"""
schedule_posts.py — Threads自動予約スクリプト

Usage:
    python scripts/schedule_posts.py --dry-run     # テスト（APIへ送信しない）
    python scripts/schedule_posts.py --execute     # 本番実行
"""

import argparse
import csv
import io
import json
import logging
import os
import sys
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from pathlib import Path
from zoneinfo import ZoneInfo

# Windowsコンソールの文字化け対策
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import yaml
from dotenv import load_dotenv

# プロジェクトルートをパスに追加
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scheduler.typefully_client import TypefullyClient

# ------------------------------------------------------------------
# 初期化
# ------------------------------------------------------------------

load_dotenv(ROOT / ".env")


def setup_logging(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return logging.getLogger(__name__)


def load_config() -> dict:
    with open(ROOT / "config" / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------------
# 投稿ソース読み込み
# ------------------------------------------------------------------

def load_posts_from_csv(csv_path: Path) -> list[dict]:
    posts = []
    with open(csv_path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("content", "").strip():
                posts.append(row)
    return posts


def load_posts_from_json(json_path: Path) -> list[dict]:
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


def load_posts(config: dict) -> list[dict]:
    source = config["content"]["source"]
    if source == "csv":
        return load_posts_from_csv(ROOT / config["content"]["csv_path"])
    elif source == "json":
        return load_posts_from_json(ROOT / config["content"]["json_path"])
    else:
        raise ValueError(f"未対応のソース: {source}")


# ------------------------------------------------------------------
# 投稿ログ
# ------------------------------------------------------------------

POSTED_LOG_HEADERS = ["post_id", "content_hash", "content_preview", "scheduled_at", "draft_id"]


def load_posted_log(log_path: Path) -> list[dict]:
    if not log_path.exists():
        return []
    with open(log_path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def append_posted_log(log_path: Path, entry: dict) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not log_path.exists()
    with open(log_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=POSTED_LOG_HEADERS)
        if write_header:
            writer.writeheader()
        writer.writerow(entry)


def content_hash(text: str) -> str:
    import hashlib
    return hashlib.md5(text.strip().encode("utf-8")).hexdigest()


# ------------------------------------------------------------------
# 重複チェック
# ------------------------------------------------------------------

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.strip(), b.strip()).ratio()


def is_duplicate(content: str, posted_log: list[dict], threshold: float) -> bool:
    h = content_hash(content)
    for entry in posted_log:
        # ハッシュ完全一致
        if entry.get("content_hash") == h:
            return True
        # テキスト類似度チェック
        preview = entry.get("content_preview", "")
        if preview and similarity(content, preview) >= threshold:
            return True
    return False


# ------------------------------------------------------------------
# スケジュール日時計算
# ------------------------------------------------------------------

def build_schedule_datetimes(
    schedule_times: list[str],
    timezone_str: str,
    target_date: date,
) -> list[datetime]:
    """
    指定日の各スケジュール時刻をタイムゾーン付きdatetimeで返す。
    すでに過去の時刻は翌日にずらす。
    """
    tz = ZoneInfo(timezone_str)
    now = datetime.now(tz)
    result = []
    for t in schedule_times:
        h, m = map(int, t.split(":"))
        dt = datetime(target_date.year, target_date.month, target_date.day, h, m, tzinfo=tz)
        if dt <= now:
            dt += timedelta(days=1)
        # UTC変換（APIはUTCで受け取る）
        result.append(dt.astimezone(ZoneInfo("UTC")))
    return result


# ------------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------------

def run(dry_run: bool) -> None:
    config = load_config()
    log_path = ROOT / config["logging"]["log_path"]
    posted_log_path = ROOT / config["logging"]["posted_log_path"]
    logger = setup_logging(log_path)

    mode = "DRY-RUN" if dry_run else "EXECUTE"
    logger.info("===== Threads予約スクリプト開始 [%s] =====", mode)

    api_key = os.getenv("TYPEFULLY_API_KEY")
    if not api_key:
        logger.error(".env に TYPEFULLY_API_KEY が設定されていません")
        sys.exit(1)

    social_set_id = config["typefully"]["social_set_id"]
    platform = config["typefully"]["platform"]
    timezone_str = config["posting"]["timezone"]
    post_count = config["posting"]["post_count_per_day"]
    schedule_times = config["posting"]["schedule_times"]
    similarity_threshold = config["duplicate_check"]["similarity_threshold"]

    # 投稿ロード
    all_posts = load_posts(config)
    logger.info("投稿ソース読み込み: %d 件", len(all_posts))

    # 過去ログロード
    posted_log = load_posted_log(posted_log_path)
    logger.info("過去ログ: %d 件", len(posted_log))

    # 重複除外
    candidates = []
    for post in all_posts:
        content = post.get("content", "").strip()
        if not content:
            continue
        if is_duplicate(content, posted_log, similarity_threshold):
            logger.info("スキップ（重複）: %s...", content[:30])
        else:
            candidates.append(post)

    logger.info("候補投稿（重複除外後）: %d 件", len(candidates))

    if not candidates:
        logger.warning("投稿候補が0件です。posts/ にコンテンツを追加してください。")
        return

    # 今日のスケジュール時刻を計算
    target_date = date.today()
    schedule_datetimes = build_schedule_datetimes(schedule_times, timezone_str, target_date)

    # 投稿数を上限に合わせる
    posts_to_schedule = candidates[:post_count]
    slots = schedule_datetimes[:len(posts_to_schedule)]

    if not dry_run:
        client = TypefullyClient(api_key)

    scheduled_count = 0
    for post, publish_at in zip(posts_to_schedule, slots):
        content = post.get("content", "").strip()
        local_time = publish_at.astimezone(ZoneInfo(timezone_str)).strftime("%Y-%m-%d %H:%M %Z")

        logger.info("予約: [%s] %s...", local_time, content[:40])

        if dry_run:
            draft_id = "dry-run-id"
        else:
            try:
                result = client.create_draft(
                    social_set_id=social_set_id,
                    content=content,
                    publish_at=publish_at,
                    platform=platform,
                )
                draft_id = result.get("id", "unknown")
                logger.info("Typefully登録成功: draft_id=%s", draft_id)
            except Exception as e:
                logger.error("Typefully登録失敗: %s", e)
                continue

        # ログ保存
        entry = {
            "post_id": post.get("id", ""),
            "content_hash": content_hash(content),
            "content_preview": content[:100],
            "scheduled_at": local_time,
            "draft_id": draft_id,
        }
        if not dry_run:
            append_posted_log(posted_log_path, entry)

        scheduled_count += 1

    logger.info("===== 完了: %d 件予約 [%s] =====", scheduled_count, mode)


# ------------------------------------------------------------------
# エントリーポイント
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Threads Typefully 予約スクリプト")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="テスト実行（APIへ送信しない）")
    group.add_argument("--execute", action="store_true", help="本番実行")
    args = parser.parse_args()
    run(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
