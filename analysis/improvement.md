# improvement.md — analysis内改善案の自動フィードバックルール

analysis/ 内で発見した改善案を
knowledge/ threads/ line/ forms/ blog/ asp/ の各ファイルに
どのタイミングで・何を反映するかを定義するルールブック。

---

## フィードバックの基本原則

1. **データ根拠を必ず持つ：** 「なんとなく」ではなく、どの指標がどう変化したから改善するのかを明記する
2. **1度に変える変数は1つ：** 複数を同時に変えると効果の原因がわからなくなる
3. **変更したら記録する：** 何をいつ変えたかを改善ログに残す
4. **効果を翌週・翌月に確認する：** 変更後の数値変化を必ず追う

---

## フィードバックルール一覧（アラート別）

### Threadsパフォーマンス悪化時

| アラート | 原因分析先 | フィードバック先 | 反映内容 |
|---------|---------|-------------|---------|
| いいね率 < 1%（T-3） | viral_analysis.md / content_analysis.md | threads/hooks.md | 弱いフックを特定し、使用停止・代替フックを追加する |
| いいね率 < 1%（T-3） | content_analysis.md | threads/post_templates.md | 低パフォーマンスの型の使用頻度を下げる |
| 保存率 < 0.5%（T-4） | content_analysis.md | threads/generate_posts.md | ノウハウ・チェックリスト型の比率を上げる指示を追加する |
| プロフィール遷移 < 1%（T-5） | viral_analysis.md | threads/cta.md | CTA投稿の文章を改善する |
| 投稿停止（T-6） | - | posts.csv | 手動で補充投稿を追加する |

---

### LINE悪化時

| アラート | 原因分析先 | フィードバック先 | 反映内容 |
|---------|---------|-------------|---------|
| 友達追加数 < 10人（L-1） | line_analysis.md | threads の投稿にLINE誘導を強化 | threads/cta.md のLINE誘導テキストを改善 |
| ブロック率 > 10%（L-2） | line_analysis.md | line/broadcast.md | 配信頻度を週2回→週1回に下げる |
| ブロック率 > 10%（L-2） | line_analysis.md | line/step_messages.md | 各Dayのメッセージを短縮する・売り込み色を下げる |
| フォーム誘導率 < 15%（L-3） | line_analysis.md | line/step_messages.md | Day3・Day5・Day7のCTAコピーを改善する |
| 相談予約率 < 30%（L-5） | line_analysis.md | line/reply_templates.md | フォーム後返信テンプレートの個人感を強化する |

---

### フォーム悪化時

| アラート | 原因分析先 | フィードバック先 | 反映内容 |
|---------|---------|-------------|---------|
| 回答完了率 < 35%（F-2） | forms_analysis.md | forms/logic.md | 質問数を5問→3問に削減する案を検討 |
| 回答完了率 < 35%（F-2） | forms_analysis.md | forms/questions.md | 最も離脱が多い質問を見直す |
| 相談予約率 < 30%（F-3） | forms_analysis.md | line/reply_templates.md | フォーム後の返信スピードと文章を改善する |

---

### ブログ悪化時

| アラート | 原因分析先 | フィードバック先 | 反映内容 |
|---------|---------|-------------|---------|
| 主要KW圏外（B-4） | blog_analysis.md | blog/update_rules.md | リライト対象記事を特定し、H2・文字数を競合と比較して改善する |
| 滞在時間 < 1分（B-2） | blog_analysis.md | blog/article_templates.md | 冒頭構成（共感→解決宣言）を強化する |
| LINE登録CVR < 0.1%（B-5） | blog_analysis.md | blog/article_templates.md | LINE誘導ブロックを本文中1回→2回に増やす |

---

### ASP悪化時

| アラート | 原因分析先 | フィードバック先 | 反映内容 |
|---------|---------|-------------|---------|
| 承認率 < 15%（A-4） | asp_analysis.md | asp/selection_rules.md | NG条件を強化する（否認理由から特定） |
| 登録率 < 30%（A-2） | asp_analysis.md | asp/copywriting.md | 紹介テンプレートの文章を改善する |
| 面談率 < 40%（A-3） | asp_analysis.md | asp/offer_flow.md | 登録後のフォロー頻度を「翌日・3日後・7日後」に見直す |

---

## 月次フィードバックルーティン

毎月最終月曜日に以下の順番で実施する。

```
Step1：monthly_review.md を完成させる（30分）

Step2：各分析ファイルのサマリーをまとめる（20分）
  → viral_analysis.md
  → content_analysis.md
  → line_analysis.md
  → forms_analysis.md
  → blog_analysis.md
  → asp_analysis.md

Step3：改善案をまとめて優先順位を付ける（10分）
  → 最も数値インパクトが大きい改善を1位にする

Step4：各フォルダに反映する（30分）
  → 上記のフィードバックルール表を参照して実施
  → 変更したファイルを改善ログに記録する

Step5：翌月のアラート閾値を見直す（5分）
  → フェーズが変わった場合は alerts.md の目標値を更新する
```

---

## 月次フィードバック先まとめ

| 反映先フォルダ | 主な更新対象ファイル |
|------------|----------------|
| knowledge/ | target.md（属性傾向）/ faq.md（頻出質問）/ objections.md（頻出不安）/ asp.md（成約実績） |
| threads/ | hooks.md（弱いフック除去）/ post_templates.md（型比率）/ viral_patterns.md（勝ちパターン）/ generate_posts.md（生成ルール）/ improvement.md |
| line/ | step_messages.md（CTA改善）/ broadcast.md（頻度・内容）/ reply_templates.md（個人感）/ conversion.md / improvement.md |
| forms/ | questions.md（選択肢）/ logic.md（問数・分岐）/ conversion.md / improvement.md |
| blog/ | article_templates.md（CTA位置）/ update_rules.md（リライト対象）/ internal_links.md / improvement.md |
| asp/ | selection_rules.md（NG条件）/ copywriting.md（紹介文）/ offer_flow.md（フォロー）/ improvement.md |

---

## 改善ログ（採用済み・全フォルダ横断）

| 日付 | 発見元ファイル | 改善内容 | 反映先ファイル | 効果（確認日・結果） |
|-----|------------|---------|------------|----------------|
| 記録なし | - | - | - | - |

---

## 改善ログ（却下・保留）

| 日付 | 提案内容 | 却下・保留理由 |
|-----|---------|------------|
| 記録なし | - | - |

---

## TODO

- [ ] 月次フィードバックルーティンをカレンダーに毎月最終月曜日で登録する
- [ ] 改善ログはGoogleドキュメントで一元管理することを検討する
- [ ] フェーズ2（友達100人超・記事10本超）になったらこのルール全体を見直す
