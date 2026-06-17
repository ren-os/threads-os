# analyze.md — 全チャネル分析フロー

Threads・LINE・フォーム・ブログ・ASP の数値を分析し、
analysis/ フォルダへ反映するための実行手順を定義する。

---

## 分析の実施タイミング

| 頻度 | 実施日 | 所要時間 |
|-----|-------|---------|
| 週次 | 毎週月曜 | 30分（簡易） |
| 月次 | 毎月最終月曜 | 90分（深掘り） |

---

## 週次分析フロー（毎週月曜・30分）

### 1. Threads分析（10分）

```
実行手順：
1. Threadsアプリ or アナリティクスで前週の投稿データを確認する
2. 以下を記録する：
   - 投稿数
   - 合計インプレッション・平均インプレッション
   - いいね数・いいね率
   - 保存数・保存率
   - プロフィール遷移数
3. analysis/viral_analysis.md の「週次バズチェック」を記入する
4. analysis/dashboard.md のThreads欄を更新する
```

### 2. LINE分析（5分）

```
実行手順：
1. LINE公式管理画面を開く
2. 前週の友達追加数・ブロック数を確認する
3. フォームリンクのクリック数を確認する（bitly等）
4. analysis/dashboard.md のLINE欄を更新する
```

### 3. フォーム分析（5分）

```
実行手順：
1. Googleフォームの管理画面を開く
2. 前週の回答数・送信完了数を確認する
3. analysis/dashboard.md のフォーム欄を更新する
```

### 4. ASP分析（5分）

```
実行手順：
1. ASP管理画面を開く（月次は1日に実施・週次は変動分を確認）
2. 新着承認・否認・ペンディングを確認する
3. asp/tracking.md の承認待ち案件リストを更新する
4. analysis/dashboard.md のASP欄を更新する
```

### 5. ブログ分析（5分）

```
実行手順：
1. Googleサーチコンソールを開く
2. 主要キーワードの順位変動（前週比）を確認する
3. 圏外に落ちた記事があれば analysis/blog_analysis.md にメモする
4. analysis/dashboard.md のブログ欄を更新する
```

---

## 月次分析フロー（毎月最終月曜・90分）

### 1. Threads深掘り分析（20分）

```
実行手順：
1. 前月の全投稿データを収集する
2. analysis/viral_analysis.md の月次深掘り分析テンプレートを記入する
3. analysis/content_analysis.md を記入する：
   - ジャンル別パフォーマンス
   - 型別パフォーマンス
   - 時間帯別パフォーマンス
   - CTA別効果
   - フック別効果
4. 勝ちパターン・負けパターンを言語化する
```

### 2. LINE深掘り分析（15分）

```
実行手順：
1. 前月のLINE全指標を収集する
2. analysis/line_analysis.md の月次分析テンプレートを記入する
3. 離脱ポイント（ブロックタイミング）を分析する
4. フォーム誘導・相談率の変化要因を仮説立てる
```

### 3. フォーム深掘り分析（15分）

```
実行手順：
1. 前月のGoogleフォーム全回答をエクスポートして確認する
2. analysis/forms_analysis.md の月次分析テンプレートを記入する
3. Q1〜Q5 の回答分布を集計する
4. forms/responses.md の月次蓄積テーブルを更新する
```

### 4. ブログ深掘り分析（20分）

```
実行手順：
1. Googleアナリティクスで前月のPV・滞在時間・直帰率を確認する
2. Googleサーチコンソールで前月のCTR・順位を確認する
3. analysis/blog_analysis.md の月次分析テンプレートを記入する
4. リライト候補記事を特定する（blog/update_rules.md に追記）
```

### 5. ASP深掘り分析（20分）

```
実行手順：
1. ASP管理画面で前月の全承認・否認・ペンディングを確認する
2. asp/tracking.md の月次承認状況サマリーを更新する
3. analysis/asp_analysis.md の月次分析テンプレートを記入する
4. 案件別CVRを計算して比較する
5. 否認理由を集計し、selection_rules.md の更新が必要か判断する
```

---

## 分析結果の反映先マッピング

| 分析ファイル | 反映先（即時） | 反映先（月次） |
|-----------|------------|------------|
| viral_analysis.md | threads/hooks.md（低パフォーマンスフック除去） | threads/viral_patterns.md |
| content_analysis.md | threads/post_templates.md（使用比率） | threads/generate_posts.md |
| line_analysis.md | line/step_messages.md（CTA改善） | line/improvement.md |
| forms_analysis.md | forms/questions.md（選択肢更新） | forms/improvement.md |
| blog_analysis.md | blog/update_rules.md（リライト対象） | blog/improvement.md |
| asp_analysis.md | asp/selection_rules.md（NG条件） | asp/improvement.md |

> 反映の詳細ルールは analysis/improvement.md と automation/improve.md を参照

---

## 分析ログ（月次更新）

| 月 | 実施日 | 主な発見 | 反映したファイル数 |
|--|-------|---------|--------------|
| 2026年6月 | - | 初月（データ計測前） | 0 |
| 2026年7月 | - | - | - |

---

## TODO

- [ ] 各ツールのアカウントが開設されたら、データ取得の具体的な手順をここに追記する
- [ ] 月次分析のプロンプト（Claude用）を生成する仕組みを将来的に設計する
- [ ] Googleスプレッドシートで自動集計できる仕組みを検討する
