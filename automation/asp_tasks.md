# asp_tasks.md — ASP運用タスク定義

案件紹介〜成果承認までのASP運用タスクを定義する。

---

## 日次タスク（相談がある日）

| タスク | 参照 | 所要時間 |
|-------|-----|---------|
| 相談ヒアリング・案件選定 | asp/selection_rules.md | 30〜60分 |
| 紹介メッセージ送信 | asp/copywriting.md | 5〜10分 |
| 相談後フォローアップ送信 | asp/copywriting.md | 5分 |
| asp/tracking.md の紹介ログを更新 | asp/tracking.md | 5分 |

---

## 週次タスク（毎週月曜）

| タスク | 参照 | 所要時間 |
|-------|-----|---------|
| ASP管理画面で新着承認・否認を確認 | asp/tracking.md | 5分 |
| 承認待ち案件リストを更新 | asp/tracking.md | 5分 |
| 登録後フォロー中ユーザーに進捗確認送信 | asp/offer_flow.md | 5〜10分 |
| 否認があれば原因をtracking.mdに記録 | asp/tracking.md | 5分 |

---

## 月次タスク（毎月1日）

| タスク | 参照 | 所要時間 |
|-------|-----|---------|
| ASP管理画面で月次承認状況を確認 | asp/tracking.md | 10分 |
| asp/tracking.md 月次サマリーを更新 | asp/tracking.md | 10分 |
| asp/kpi.md 月次サマリーを作成 | asp/kpi.md | 10分 |
| asp_analysis.md 月次テンプレートを記入 | analysis/asp_analysis.md | 20分 |
| 否認理由を集計してselection_rules.mdを更新 | asp/selection_rules.md | 10分 |
| 承認率の低い案件の継続可否を判断 | asp/improvement.md | 10分 |

---

## 案件紹介フロー（相談後・毎回）

```
Step1：ヒアリング（相談中に実施）
→ asp/offer_flow.md フェーズ1〜2を実行
→ 年齢・雇用形態・希望職種・地域をメモ

Step2：案件選定
→ asp/selection_rules.md の YES/NO フローを実行
→ NG条件チェックリストを確認

Step3：紹介
→ asp/copywriting.md の属性別テンプレートを選んで送信

Step4：フォローアップ
→ 翌日：「登録できましたか？」確認メッセージ
→ 登録後3日：進捗確認メッセージ
→ 初回面談前日：事前アドバイスメッセージ
→ 初回面談後：フォローメッセージ

Step5：トラッキング
→ asp/tracking.md の紹介ログに全ステップを記録
```

---

## ASP初期設定タスク（一度限り）

```
□ 第二新卒エージェントneoのASPアカウントを確認・設定する
□ 就職カレッジのASPアカウントを確認・設定する
□ UZUZのASPに登録する ← TODO
□ キャリアスタートのASPに登録する ← TODO
□ 各案件のアフィリエイトリンクを取得してservices.mdに記入する
□ ASP管理画面の確認方法・承認確認ページをブックマークする
□ 毎月1日の「ASP管理画面確認」をカレンダーに登録する
```

---

## 否認対応フロー

```
否認が発生した場合：
1. asp/tracking.md の否認ログに記録する（日付・案件・理由）
2. 否認理由を asp/services.md の NG条件と照合する
3. NG条件のすり抜けだった場合 → asp/selection_rules.md を更新する
4. 原因不明の場合 → ASPサポートに問い合わせる
5. 否認が3件連続したら → analysis/alerts.md A-5 のアクションを実施する
```

---

## TODO

- [ ] UZUZ・キャリアスタートのASP登録を完了させる
- [ ] 各案件の報酬単価・成果条件を確認してservices.mdに記入する
- [ ] 案件紹介数が月5件を超えたら、tracking.md をGoogleスプレッドシートに移行する
