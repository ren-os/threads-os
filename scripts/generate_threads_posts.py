"""
generate_threads_posts.py
Threads投稿ストックCSVの管理ユーティリティ
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
STOCK_CSV = ROOT / "posts" / "threads_posts_stock.csv"

HEADERS = ["id", "category", "pattern", "hook", "body", "cta", "diagnosis_intent", "status", "created_at"]


def load_stock() -> list[dict]:
    if not STOCK_CSV.exists():
        return []
    with open(STOCK_CSV, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _save_stock(rows: list[dict]) -> None:
    with open(STOCK_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)


def get_next_id(rows: list[dict]) -> int:
    if not rows:
        return 1
    return max(int(r["id"]) for r in rows) + 1


def show_stats() -> None:
    rows = load_stock()
    total = len(rows)
    drafted = sum(1 for r in rows if r["status"] == "draft")
    posted  = sum(1 for r in rows if r["status"] == "posted")

    print(f"\n📊 投稿ストック統計")
    print(f"  合計   : {total} 本")
    print(f"  draft  : {drafted} 本")
    print(f"  posted : {posted} 本")

    print(f"\n📁 カテゴリ別 draft 残数")
    categories = ["面接官", "元人事", "ブラック企業", "第二新卒", "フリーター"]
    for cat in categories:
        n = sum(1 for r in rows if r["category"] == cat and r["status"] == "draft")
        bar = "█" * n + "░" * max(0, 10 - n)
        print(f"  {cat:8s} : {bar} {n}/10")

    print(f"\n🎯 diagnosis_intent 別 draft")
    for intent in ["high", "medium", "low"]:
        n = sum(1 for r in rows if r["diagnosis_intent"] == intent and r["status"] == "draft")
        print(f"  {intent:6s} : {n} 本")


def format_post(row: dict) -> str:
    """hook + body + cta を結合して投稿テキストを生成する。"""
    parts = [row["hook"]]
    body = row["body"].replace("\\n", "\n")
    if body:
        parts.append("")
        parts.append(body)
    if row.get("cta"):
        parts.append("")
        parts.append(row["cta"])
    return "\n".join(parts)


def get_draft_posts(category: str = None) -> list[dict]:
    rows = load_stock()
    drafts = [r for r in rows if r["status"] == "draft"]
    if category:
        drafts = [r for r in drafts if r["category"] == category]
    return drafts


def get_high_intent_posts() -> list[dict]:
    rows = load_stock()
    return [r for r in rows if r["status"] == "draft" and r["diagnosis_intent"] == "high"]


def pick_next_posts(n: int = 5) -> list[dict]:
    """次に投稿すべきn本を返す（high優先 → medium → low）。"""
    rows = load_stock()
    drafts = [r for r in rows if r["status"] == "draft"]
    high   = [r for r in drafts if r["diagnosis_intent"] == "high"]
    medium = [r for r in drafts if r["diagnosis_intent"] == "medium"]
    low    = [r for r in drafts if r["diagnosis_intent"] == "low"]
    return (high + medium + low)[:n]


def mark_as_posted(post_id: int) -> None:
    rows = load_stock()
    found = False
    for r in rows:
        if int(r["id"]) == post_id:
            r["status"] = "posted"
            found = True
    if found:
        _save_stock(rows)
        print(f"✅ ID {post_id} を posted に更新しました")
    else:
        print(f"❌ ID {post_id} が見つかりません")


def show_post(post_id: int) -> None:
    rows = load_stock()
    for r in rows:
        if int(r["id"]) == post_id:
            print(f"\n--- ID {r['id']} [{r['category']} / {r['pattern']}] intent={r['diagnosis_intent']} ---")
            print(format_post(r))
            return
    print(f"❌ ID {post_id} が見つかりません")


def show_next(n: int = 5) -> None:
    posts = pick_next_posts(n)
    print(f"\n📝 次の {n} 本（投稿候補）\n")
    for post in posts:
        print(f"{'─'*50}")
        print(f"ID {post['id']} [{post['category']} / {post['pattern']}] intent={post['diagnosis_intent']}")
        print(format_post(post))
    print(f"{'─'*50}")


# ─── CLI ───
if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] == "stats":
        show_stats()

    elif args[0] == "next":
        n = int(args[1]) if len(args) > 1 else 5
        show_next(n)

    elif args[0] == "show" and len(args) > 1:
        show_post(int(args[1]))

    elif args[0] == "post" and len(args) > 1:
        mark_as_posted(int(args[1]))

    elif args[0] == "high":
        posts = get_high_intent_posts()
        print(f"\n🎯 high intent の未投稿: {len(posts)} 本\n")
        for p in posts:
            print(f"ID {p['id']} [{p['category']}] {p['hook']}")

    else:
        print("使い方:")
        print("  python scripts/generate_threads_posts.py stats      # 統計表示")
        print("  python scripts/generate_threads_posts.py next [n]   # 次のn本を表示")
        print("  python scripts/generate_threads_posts.py show <id>  # 投稿内容を表示")
        print("  python scripts/generate_threads_posts.py post <id>  # 投稿済みにする")
        print("  python scripts/generate_threads_posts.py high        # high intent一覧")
