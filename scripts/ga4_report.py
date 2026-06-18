"""
ga4_report.py — GA4 Data API を使って日次・週次レポートを生成する

使い方:
  python scripts/ga4_report.py daily        # 昨日のレポート
  python scripts/ga4_report.py weekly       # 直近7日のレポート
  python scripts/ga4_report.py both         # 両方（デフォルト）
  python scripts/ga4_report.py daily --date 20260618

必要な環境変数（.env に記載）:
  GA4_PROPERTY_ID              — 数値のみ（GA4管理 > プロパティ設定 > プロパティID）
  GOOGLE_APPLICATION_CREDENTIALS — サービスアカウントJSONのパス
"""
import os
import argparse
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    OrderBy,
    RunReportRequest,
)

load_dotenv()

PROPERTY_ID = os.getenv("GA4_PROPERTY_ID", "")
ANALYSIS_DIR = Path(__file__).parent.parent / "analysis"

# utm_campaign → 投稿シリーズ名の対応表
CAMPAIGN_LABELS: dict[str, str] = {
    "career_diagnosis_interview": "面接官シリーズ",
    "career_diagnosis_jinjika":   "元人事シリーズ",
    "career_diagnosis_black":     "ブラック企業シリーズ",
    "career_diagnosis_daini":     "第二新卒シリーズ",
    "career_diagnosis_freeter":   "フリーターシリーズ",
}

# KPI 閾値（良・注意・危険）
KPI = {
    "start_rate":    {"good": 40, "warn": 20},
    "complete_rate": {"good": 70, "warn": 40},
    "cta_rate":      {"good": 15, "warn": 8},
}


# ──────────────────────────────────────────────
# GA4 クエリ
# ──────────────────────────────────────────────

def _client() -> BetaAnalyticsDataClient:
    if not PROPERTY_ID:
        raise RuntimeError(
            "GA4_PROPERTY_ID が未設定です。.env に数値プロパティIDを記入してください。"
        )
    return BetaAnalyticsDataClient()


def _prop() -> str:
    return f"properties/{PROPERTY_ID}"


def fetch_event_totals(client, start: str, end: str) -> dict[str, int]:
    """指定期間のイベント名別合計を返す"""
    req = RunReportRequest(
        property=_prop(),
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[Dimension(name="eventName")],
        metrics=[Metric(name="eventCount")],
    )
    resp = client.run_report(req)
    return {
        row.dimension_values[0].value: int(row.metric_values[0].value)
        for row in resp.rows
    }


def fetch_by_campaign(client, start: str, end: str) -> list[dict]:
    """utm_campaign(=sessionCampaignName) × イベント名 の集計を返す"""
    req = RunReportRequest(
        property=_prop(),
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[
            Dimension(name="sessionCampaignName"),
            Dimension(name="eventName"),
        ],
        metrics=[Metric(name="eventCount")],
        order_bys=[
            OrderBy(
                metric=OrderBy.MetricOrderBy(metric_name="eventCount"),
                desc=True,
            )
        ],
    )
    resp = client.run_report(req)
    return [
        {
            "campaign": row.dimension_values[0].value,
            "event":    row.dimension_values[1].value,
            "count":    int(row.metric_values[0].value),
        }
        for row in resp.rows
    ]


def fetch_daily(client, start: str, end: str) -> list[dict]:
    """日付 × イベント名 の集計を返す（週次レポート用）"""
    req = RunReportRequest(
        property=_prop(),
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[
            Dimension(name="date"),
            Dimension(name="eventName"),
        ],
        metrics=[Metric(name="eventCount")],
        order_bys=[
            OrderBy(
                dimension=OrderBy.DimensionOrderBy(dimension_name="date"),
            )
        ],
    )
    resp = client.run_report(req)
    return [
        {
            "date":  row.dimension_values[0].value,
            "event": row.dimension_values[1].value,
            "count": int(row.metric_values[0].value),
        }
        for row in resp.rows
    ]


# ──────────────────────────────────────────────
# 計算ユーティリティ
# ──────────────────────────────────────────────

def calc_rates(counts: dict[str, int]) -> dict:
    pv       = counts.get("page_view", 0)
    start    = counts.get("start_diagnosis", 0)
    complete = counts.get("complete_diagnosis", 0)
    cta      = counts.get("cta_click", 0)
    return {
        "pv":            pv,
        "start":         start,
        "complete":      complete,
        "cta":           cta,
        "start_rate":    round(start    / pv       * 100, 1) if pv       else 0.0,
        "complete_rate": round(complete / start    * 100, 1) if start    else 0.0,
        "cta_rate":      round(cta      / complete * 100, 1) if complete else 0.0,
    }


def status(value: float, key: str) -> str:
    t = KPI[key]
    if value >= t["good"]:
        return "✅"
    elif value >= t["warn"]:
        return "⚠️"
    return "🔴"


def fmt_date(yyyymmdd: str) -> str:
    return f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:]}"


def pivot_campaigns(rows: list[dict]) -> dict[str, dict[str, int]]:
    """campaign → {eventName: count} の二重辞書を返す"""
    out: dict[str, dict[str, int]] = {}
    for row in rows:
        c = row["campaign"]
        out.setdefault(c, {})[row["event"]] = row["count"]
    return out


# ──────────────────────────────────────────────
# レポートビルダー
# ──────────────────────────────────────────────

def build_daily_report(
    counts: dict[str, int],
    campaign_rows: list[dict],
    target_date: str,
) -> str:
    r  = calc_rates(counts)
    cp = pivot_campaigns(campaign_rows)

    lines = [
        f"# 日次レポート — {fmt_date(target_date)}",
        "",
        "> 自動生成: `scripts/ga4_report.py`  |  測定ID: G-R3JPL9E7TM",
        "",
        "---",
        "",
        "## サマリー",
        "",
        "| 指標 | 値 | 目標 | 状態 |",
        "|-----|---|-----|-----|",
        f"| PV | {r['pv']:,} | — | — |",
        f"| 診断開始数 | {r['start']:,} | — | — |",
        f"| 診断開始率 | {r['start_rate']}% | 40%以上 | {status(r['start_rate'], 'start_rate')} |",
        f"| 診断完了数 | {r['complete']:,} | — | — |",
        f"| 診断完了率 | {r['complete_rate']}% | 70%以上 | {status(r['complete_rate'], 'complete_rate')} |",
        f"| CTAクリック数 | {r['cta']:,} | — | — |",
        f"| CTAクリック率 | {r['cta_rate']}% | 15%以上 | {status(r['cta_rate'], 'cta_rate')} |",
        "",
        "---",
        "",
        "## 流入元 (utm_campaign) 別",
        "",
    ]

    if cp:
        lines += [
            "| utm_campaign | ラベル | PV | 診断開始 | 診断完了 | CTAクリック | 完了率 |",
            "|-------------|-------|---|--------|--------|-----------|------|",
        ]
        for campaign, events in sorted(cp.items(), key=lambda x: x[1].get("complete_diagnosis", 0), reverse=True):
            label       = CAMPAIGN_LABELS.get(campaign, campaign)
            cstart      = events.get("start_diagnosis", 0)
            ccomplete   = events.get("complete_diagnosis", 0)
            ccta        = events.get("cta_click", 0)
            cpv         = events.get("page_view", 0)
            comp_rate   = round(ccomplete / cstart * 100, 1) if cstart else 0.0
            lines.append(
                f"| `{campaign}` | {label} | {cpv} | {cstart} | {ccomplete} | {ccta} | {comp_rate}% |"
            )
    else:
        lines.append("_データなし（utm未設定の直接流入のみ）_")

    lines += [
        "",
        "---",
        "",
        "## Threads投稿シリーズ別",
        "",
        "| 投稿シリーズ | utm_campaign | 診断完了数 | CTAクリック数 |",
        "|-----------|-------------|---------|------------|",
    ]
    for campaign, label in CAMPAIGN_LABELS.items():
        events    = cp.get(campaign, {})
        ccomplete = events.get("complete_diagnosis", 0)
        ccta      = events.get("cta_click", 0)
        lines.append(f"| {label} | `{campaign}` | {ccomplete} | {ccta} |")

    lines += [
        "",
        "---",
        "",
        "## 今日の気づき・アクション",
        "",
        "- [ ] （毎日ここに1行メモする）",
        "",
        "---",
        f"_最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
    ]
    return "\n".join(lines)


def build_weekly_report(
    daily_rows: list[dict],
    campaign_rows: list[dict],
    start: str,
    end: str,
) -> str:
    # 日付 × イベント の二重辞書
    daily_pivot: dict[str, dict[str, int]] = {}
    for row in daily_rows:
        daily_pivot.setdefault(row["date"], {})[row["event"]] = row["count"]

    # 週全体の合計
    total: dict[str, int] = {}
    for events in daily_pivot.values():
        for ev, cnt in events.items():
            total[ev] = total.get(ev, 0) + cnt
    r  = calc_rates(total)
    cp = pivot_campaigns(campaign_rows)

    lines = [
        f"# 週次レポート — {fmt_date(start)} 〜 {fmt_date(end)}",
        "",
        "> 自動生成: `scripts/ga4_report.py`  |  測定ID: G-R3JPL9E7TM",
        "",
        "---",
        "",
        "## 週間サマリー",
        "",
        "| 指標 | 週合計 | 目標 | 状態 |",
        "|-----|------|-----|-----|",
        f"| PV | {r['pv']:,} | — | — |",
        f"| 診断開始数 | {r['start']:,} | — | — |",
        f"| 診断開始率 | {r['start_rate']}% | 40%以上 | {status(r['start_rate'], 'start_rate')} |",
        f"| 診断完了数 | {r['complete']:,} | — | — |",
        f"| 診断完了率 | {r['complete_rate']}% | 70%以上 | {status(r['complete_rate'], 'complete_rate')} |",
        f"| CTAクリック数 | {r['cta']:,} | — | — |",
        f"| CTAクリック率 | {r['cta_rate']}% | 15%以上 | {status(r['cta_rate'], 'cta_rate')} |",
        "",
        "---",
        "",
        "## 日別トレンド",
        "",
        "| 日付 | PV | 診断開始 | 開始率 | 診断完了 | 完了率 | CTAクリック | CTA率 |",
        "|-----|---|--------|------|--------|------|-----------|-----|",
    ]
    for date in sorted(daily_pivot.keys()):
        dr = calc_rates(daily_pivot[date])
        lines.append(
            f"| {fmt_date(date)} | {dr['pv']} | {dr['start']} | {dr['start_rate']}% | "
            f"{dr['complete']} | {dr['complete_rate']}% | {dr['cta']} | {dr['cta_rate']}% |"
        )

    lines += [
        "",
        "---",
        "",
        "## utm_campaign 別（週次）",
        "",
    ]
    if cp:
        lines += [
            "| utm_campaign | ラベル | PV | 診断開始 | 診断完了 | CTAクリック | 完了率 |",
            "|-------------|-------|---|--------|--------|-----------|------|",
        ]
        for campaign, events in sorted(cp.items(), key=lambda x: x[1].get("complete_diagnosis", 0), reverse=True):
            label     = CAMPAIGN_LABELS.get(campaign, campaign)
            cstart    = events.get("start_diagnosis", 0)
            ccomplete = events.get("complete_diagnosis", 0)
            ccta      = events.get("cta_click", 0)
            cpv       = events.get("page_view", 0)
            comp_rate = round(ccomplete / cstart * 100, 1) if cstart else 0.0
            lines.append(
                f"| `{campaign}` | {label} | {cpv} | {cstart} | {ccomplete} | {ccta} | {comp_rate}% |"
            )
    else:
        lines.append("_データなし（utm未設定の直接流入のみ）_")

    # Threads投稿ランキング
    ranked = []
    for campaign, label in CAMPAIGN_LABELS.items():
        events    = cp.get(campaign, {})
        ccomplete = events.get("complete_diagnosis", 0)
        ccta      = events.get("cta_click", 0)
        cta_rate  = round(ccta / ccomplete * 100, 1) if ccomplete else 0.0
        ranked.append((ccomplete, ccta, cta_rate, label, campaign))
    ranked.sort(reverse=True)

    lines += [
        "",
        "---",
        "",
        "## Threads投稿シリーズ 効果ランキング（診断完了数順）",
        "",
        "| ランク | 投稿シリーズ | utm_campaign | 診断完了数 | CTAクリック数 | CTA率 |",
        "|------|-----------|-------------|---------|------------|------|",
    ]
    for i, (ccomplete, ccta, cta_rate, label, campaign) in enumerate(ranked, 1):
        lines.append(
            f"| {i} | {label} | `{campaign}` | {ccomplete} | {ccta} | {cta_rate}% |"
        )

    lines += [
        "",
        "---",
        "",
        "## 来週のアクション",
        "",
        "| 優先度 | アクション | 根拠 |",
        "|------|---------|-----|",
        "| 高 | （数値を見て記入） | — |",
        "| 中 | — | — |",
        "",
        "---",
        f"_最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
    ]
    return "\n".join(lines)


# ──────────────────────────────────────────────
# エントリポイント
# ──────────────────────────────────────────────

def generate_daily(target_date: str | None = None) -> None:
    if target_date is None:
        target_date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    client        = _client()
    counts        = fetch_event_totals(client, target_date, target_date)
    campaign_rows = fetch_by_campaign(client, target_date, target_date)
    report        = build_daily_report(counts, campaign_rows, target_date)
    out           = ANALYSIS_DIR / "daily_report.md"
    out.write_text(report, encoding="utf-8")
    print(f"✅ 日次レポート生成: {out}")


def generate_weekly(end_date: str | None = None) -> None:
    if end_date is None:
        end_date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    start_date    = (datetime.strptime(end_date, "%Y%m%d") - timedelta(days=6)).strftime("%Y%m%d")
    client        = _client()
    daily_rows    = fetch_daily(client, start_date, end_date)
    campaign_rows = fetch_by_campaign(client, start_date, end_date)
    report        = build_weekly_report(daily_rows, campaign_rows, start_date, end_date)
    out           = ANALYSIS_DIR / "weekly_report.md"
    out.write_text(report, encoding="utf-8")
    print(f"✅ 週次レポート生成: {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GA4レポート生成")
    parser.add_argument(
        "mode",
        nargs="?",
        choices=["daily", "weekly", "both"],
        default="both",
    )
    parser.add_argument("--date",     help="日次の対象日 YYYYMMDD（省略=昨日）")
    parser.add_argument("--end-date", help="週次の終了日 YYYYMMDD（省略=昨日）")
    args = parser.parse_args()

    if args.mode in ("daily", "both"):
        generate_daily(args.date)
    if args.mode in ("weekly", "both"):
        generate_weekly(args.end_date)
