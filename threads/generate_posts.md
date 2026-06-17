# generate_posts.md — 投稿自動生成プロンプト

このファイルは投稿20本を自動生成する際のメインプロンプト定義書です。
Claudeはこのファイルを読み込み、以下の手順に従って投稿を生成してください。

---

## 実行前に必ず読み込むファイル

```
1.  AGENTS.md                        ← 運営OS・最優先ルール
2.  knowledge/brand.md               ← ブランド・トーン
3.  knowledge/target.md              ← ターゲット・ペルソナ
4.  knowledge/content_pillars.md     ← 投稿比率・テーマ優先順位
5.  knowledge/posting_rules.md       ← 文字数・NG表現
6.  threads/posted_log.md            ← 投稿済みログ（重複チェック）
7.  threads/hooks.md                 ← 使用済み／未使用フック
8.  threads/viral_patterns.md        ← 伸びたパターン（実データ反映済み）
9.  threads/ideas.md                 ← ネタバンク（優先度順）
10. threads/improvement.md           ← 前回の改善指示
11. threads/kpi.md                   ← KPI目標値（現フェーズの基準を確認）
12. threads/ab_test.md               ← 勝ちパターン・進行中テストの確認
```

---

## 生成手順

### STEP 1：重複チェック

`threads/posted_log.md` を参照し、以下を確認する。

- 過去投稿のフック冒頭と被っていないか
- 同じテーマを直近10本以内に扱っていないか
- 同じ型（ストーリー/チェックリスト等）が3本連続していないか

### STEP 2：投稿比率を確認

```
体験談・ストーリー：10本（50%）
転職ノウハウ：6本（30%）
共感投稿：4本（20%）
CTA付き：2本（20本中、10投稿に1〜2本）
```

### STEP 3：投稿ジャンルのバランス確認

`knowledge/content_pillars.md` の発信テーマ優先順位に従い、
前回の投稿セットで少なかったジャンルを優先して生成する。

### STEP 4：フックを選ぶ

`threads/hooks.md` の「未使用ストック」からフックを選ぶ。
なければ新規でフックを作り、hooks.mdに追記する。

### STEP 5：投稿を生成

`threads/post_templates.md` の型を参照し、
型を毎回変えながら20本生成する。

### STEP 6：投稿前チェック

`threads/posting_checklist.md` の全項目を通過させる。
1つでも引っかかった投稿は修正する。

### STEP 7：出力

```
posts/posts.csv を上書き（既存内容を置き換える）
```

出力フォーマット：
```csv
id,content,category,created_at
1,"投稿本文",カテゴリ,YYYY-MM-DD
```

---

## 改善指示の反映

`threads/improvement.md` の「次回反映事項」を必ず確認し、
生成に反映してから投稿を作る。

## A/Bテストの反映

`threads/ab_test.md` を参照し、以下を確認してから生成する。

1. 「テスト状態：進行中」のテストがあれば、A案とB案を交互に含める
2. 「勝ちパターン保存」に記録されたパターンを標準として採用する
3. 「負けパターン記録」に記録されたパターンは使用しない

## KPI目標値の確認

`threads/kpi.md` の「現在のフェーズ目標値」を確認し、
目標を下回っている指標がある場合は、その改善を優先する。

例：いいね率が目標を下回っている → 共感投稿の比率を一時的に増やす

---

## 生成後にやること

1. `threads/posted_log.md` に20本分を追記する
2. `threads/hooks.md` の使用済みフックを移動する
3. `threads/ideas.md` から使ったネタを「使用済み」に移動する
4. 改善提案があれば `threads/improvement.md` に追記する
