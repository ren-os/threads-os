# scheduler.md — 実行スケジュール定義

REN OS の全タスクを時間軸で整理したマスタースケジュール。

---

## 毎日のスケジュール

| 時間 | タスク | 自動/手動 | 参照ファイル |
|-----|-------|---------|-----------|
| 07:00 | Threads投稿①（自動） | 自動 | main.py / posts.csv |
| 09:00 | LINE確認・返信 | 手動 | line/reply_templates.md |
| 10:00 | Threads投稿②（自動） | 自動 | main.py |
| 13:00 | Threads投稿③（自動） + フォーム確認 | 自動＋手動 | main.py / Googleフォーム |
| 18:00 | Threads投稿④（自動） | 自動 | main.py |
| 20:00 | Threads投稿⑤（自動） + コメント返信 | 自動＋手動 | main.py / Threads |
| 22:00 | 改善ログ記録（気づきがあれば） | 手動 | analysis/viral_analysis.md |

**自動化状況：**
- 投稿（5本/日）：Windows Task Scheduler → main.py で自動実行 ✅
- LINE返信：手動（TODO：将来的に高度化）
- フォーム確認：手動（TODO：通知設定で効率化可能）

---

## 毎週のスケジュール（月曜日）

| 時間 | タスク | 参照ファイル | 所要時間 |
|-----|-------|-----------|---------|
| 09:00 | dashboard.md 更新（前週数値入力） | analysis/dashboard.md | 15分 |
| 09:15 | アラート確認 | analysis/alerts.md | 5分 |
| 09:20 | weekly_review.md 記入 | analysis/weekly_review.md | 20分 |
| 09:40 | 勝ち投稿抽出・viral_analysis.md 更新 | analysis/viral_analysis.md | 10分 |
| 09:50 | 競合チェック | competitor_watch.md | 15分 |
| 10:05 | 週次改善アクション実施（1〜2個） | improve.md | 20分 |
| 10:25 | LINE週次チェック（ブロック率・フォーム誘導） | line_tasks.md | 10分 |
| 10:35 | ASP週次チェック（承認・否認・フォロー） | asp_tasks.md | 10分 |
| 10:45 | ブログ週次チェック（順位変動） | blog_tasks.md | 5分 |
| 10:50 | posts.csv 残数確認→不足なら投稿補充 | generate_posts.md | 10〜30分 |
| 11:20 | 週次レポート記録 | reports.md | 10分 |

**週次合計所要時間：約90分**

---

## 毎月のスケジュール（最終月曜日）

| 時間 | タスク | 参照ファイル | 所要時間 |
|-----|-------|-----------|---------|
| 10:00 | 月次KPIサマリー作成 | analysis/dashboard.md + 各kpi.md | 30分 |
| 10:30 | monthly_review.md 記入 | analysis/monthly_review.md | 60分 |
| 11:30 | 各フォルダへ月次フィードバック実施 | improve.md | 60分 |
| 12:30 | 翌月の投稿ネタ生成（20本以上） | generate_posts.md | 30分 |
| 13:00 | 翌月計画・目標設定 | analysis/dashboard.md | 30分 |
| 13:30 | 月次レポート記録 | reports.md | 15分 |
| 13:45 | ASP管理画面確認・月次承認チェック | asp/tracking.md | 10分 |
| 13:55 | ブログ：翌月公開記事テーマを決定 | blog/ideas.md | 10分 |
| 14:05 | LINE：翌月配信カレンダー作成 | line/broadcast.md | 10分 |

**月次合計所要時間：約4時間**

---

## 四半期スケジュール（3・6・9・12月）

| タスク | 参照ファイル | 所要時間 |
|-------|-----------|---------|
| ASP案件の入れ替え検討 | asp/improvement.md | 20分 |
| ターゲット設定の見直し | knowledge/target.md | 20分 |
| ブログカテゴリ・記事マップ更新 | blog/categories.md | 20分 |
| 競合の全体ポジション変化確認 | analysis/competitors.md | 20分 |
| alerts.md のアラート基準値を更新 | analysis/alerts.md | 10分 |
| ASP各サービスの情報更新（公式確認） | asp/services.md | 20分 |

**四半期合計所要時間：約2時間**

---

## 年次スケジュール（1月）

| タスク | 参照ファイル |
|-------|-----------|
| ブログ記事の年度表記を更新（「2027年最新」等） | blog/update_rules.md |
| 年間KPIの振り返り・翌年目標設定 | analysis/monthly_review.md |
| knowledge/ 全体の情報を最新化する | knowledge/* |

---

## 自動化済み vs 手動タスクの整理

| タスク | 現在 | 将来的に |
|-------|-----|--------|
| Threads投稿（5本/日） | ✅ 自動（Task Scheduler） | 維持 |
| 投稿生成（月次） | 手動（Claude使用） | 自動化検討（Claude API） |
| LINE返信 | 手動 | 一部自動（キーワード返信） |
| フォーム確認・返信 | 手動 | 通知設定で効率化 |
| KPIデータ集計 | 手動 | GASで自動化検討 |
| 競合チェック | 手動 | ツール導入検討 |

---

## TODO

- [ ] 週次・月次スケジュールをGoogleカレンダーに繰り返し登録する
- [ ] ASP管理画面確認を毎月1日のカレンダーに登録する
- [ ] Windows Task Schedulerの実行ログを週次でチェックする習慣を作る
