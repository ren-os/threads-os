# monthly.md — 毎月の実行内容

毎月最終月曜日に実施するルーティン。所要時間：2〜3時間。
月次KPIを確認し、戦略を見直し、翌月の計画を立てる。

---

## 月次実行スケジュール（毎月最終月曜日）

```
10:00 ── 月次KPIサマリー作成（dashboard.md + 各フォルダkpi.md）
         ↓
10:30 ── analysis/monthly_review.md を記入
         ↓
11:30 ── 勝ちパターン・負けパターンの言語化
         ↓
12:00 ── 各フォルダへの月次フィードバック実施
         ↓
13:00 ── 翌月の投稿ネタ生成（20本以上 → posts.csv 補充）
         ↓
14:00 ── 翌月の計画・目標設定
         ↓
14:30 ── 月次レポートを reports.md に記録
```

---

## タスク1：月次KPIサマリー作成（10:00・30分）

```
実行手順：
1. analysis/dashboard.md の月次データを確認する
2. 以下の各ファイルの月次サマリーを開いて数値を確認する：
   - threads/kpi.md
   - line/kpi.md
   - forms/kpi.md
   - asp/kpi.md
   - blog/kpi.md
3. 全体ファネルの転換率（Threads→LINE→フォーム→相談→ASP）を計算する
4. 先月比での増減を把握する
```

---

## タスク2：月次レビュー（10:30・60分）

```
実行手順：
1. analysis/monthly_review.md のテンプレートをコピーして記入する
2. 以下の分析ファイルを順番に確認してサマリーを転記する：
   - analysis/viral_analysis.md（バズ投稿 TOP3）
   - analysis/content_analysis.md（型・ジャンル・フック別）
   - analysis/line_analysis.md（ブロック・フォーム誘導・相談率）
   - analysis/forms_analysis.md（完了率・属性傾向）
   - analysis/blog_analysis.md（PV・順位・CVR）
   - analysis/asp_analysis.md（承認率・案件別CVR）
3. 勝ちパターン・負けパターンを3つずつ言語化する
4. 来月の改善アクションを2〜3個に絞る
```

---

## タスク3：各フォルダへの月次フィードバック（12:00・60分）

analysis/improvement.md のルールに沿って実施する。

```
実行順序：
① knowledge/ への更新
   - knowledge/target.md（フォーム属性傾向を反映）
   - knowledge/faq.md（頻出質問を追加）
   - knowledge/objections.md（頻出不安を追加）
   - knowledge/content_pillars.md（バズジャンルを反映）

② threads/ への更新
   - threads/hooks.md（低パフォーマンスフックを除去・新フックを追加）
   - threads/viral_patterns.md（勝ちパターンを追加）
   - threads/post_templates.md（使用比率の見直し）
   - threads/improvement.md（翌月反映事項を記録）

③ line/ への更新
   - line/step_messages.md（CTA改善）
   - line/broadcast.md（コンテンツネタ更新）
   - line/conversion.md（転換率改善アクション）
   - line/improvement.md（翌月反映事項を記録）

④ forms/ への更新
   - forms/questions.md（選択肢の見直し）
   - forms/responses.md（月次データを転記）
   - forms/improvement.md（翌月反映事項を記録）

⑤ blog/ への更新
   - blog/ideas.md（新記事ネタを追加）
   - blog/update_rules.md（リライト対象記事を記入）
   - blog/improvement.md（翌月改善テーマを記録）

⑥ asp/ への更新
   - asp/comparison.md（承認率実績を反映）
   - asp/selection_rules.md（否認理由からNG条件更新）
   - asp/improvement.md（翌月反映事項を記録）
```

---

## タスク4：翌月の投稿ネタ生成（13:00・30分）

```
実行手順：
1. threads/generate_posts.md の投稿生成フローを実行する
   （knowledge/ + threads/ の全参照ファイルを読み込む）
2. 20本以上の投稿を生成する
3. posts.csv に追加する
4. python main.py --dry-run で確認する（重複チェック）
5. threads/posted_log.md に新セット番号を記録する
6. threads/ideas.md の「使用済み」欄を更新する
```

---

## タスク5：翌月の計画・目標設定（14:00・30分）

```
設定する内容：
□ 各KPIの翌月目標値（analysis/dashboard.md に記入）
□ 翌月の優先改善テーマ（1〜2個に絞る）
□ 翌月公開するブログ記事（3〜4本を決める）
□ ASPで新規追加する案件（あれば）
□ LINEで試す新しい施策（あれば）
```

---

## 月次PDCAサマリー

```
P（Plan）: 先月初の目標 → 実績の差分を確認
D（Do）  : 今月実施した改善アクション
C（Check）: 改善の効果（数値変化）
A（Act）  : 翌月の改善アクション
```

---

## 月次コンプレックスチェック（四半期に1回）

3ヶ月に1度、以下を追加で実施する。

```
□ ASP案件の入れ替え検討（asp/improvement.md 参照）
□ ターゲット設定の見直し（knowledge/target.md 更新）
□ ブログのカテゴリ・記事マップ更新（blog/categories.md）
□ 競合の全体的なポジション変化を確認（analysis/competitors.md）
□ alerts.md のアラート基準値を更新する（フェーズが変わった場合）
```

---

## TODO

- [ ] 月次ルーティンを毎月最終月曜日のカレンダーに登録する
- [ ] 各フォルダへのフィードバックは必ず analysis/improvement.md の改善ログに記録する
- [ ] 月次作業の所要時間が3時間を超えるようになったらタスクを分割する
