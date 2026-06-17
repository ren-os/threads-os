# winning_posts.md — 勝ち投稿データベース

毎朝のリサーチで発見した「バズっている投稿」を最低3本/日保存するDB。
蓄積データは `knowledge/post_patterns.md` の優先度更新と
`analysis/competitive_patterns.md` の週次ランキングに使用する。

---

## このファイルの役割

```
daily_research.md で「伸びた投稿を発見する」
         ↓
winning_posts.md に「投稿の詳細を記録する」（このファイル）
         ↓
analysis/competitive_patterns.md で「週次でパターンを集計する」
         ↓
knowledge/post_patterns.md の「優先度を更新する」
         ↓
automation/generate_posts.md の「生成条件に反映する」
```

---

## 記録ルール

```
・毎朝のリサーチで各プラットフォーム最低1本（合計3本以上）を記録する
・基準：いいね50以上（Threads）/ リポスト10以上（X）/ 再生1万以上（TikTok）
・必ず全項目を埋める。URLが取れない場合はフック全文を記録する
・同じ「型」の投稿が蓄積されたら competitive_patterns.md でカウントする
```

---

## 勝ち投稿ログ

### 記録テンプレート（毎日このブロックをコピーして追記）

```
## WP-[通し番号] / 発見日：YYYY-MM-DD / プラットフォーム：[Threads/X/TikTok/Instagram/YouTube]

| 項目 | 内容 |
|-----|-----|
| 投稿URL | [URL または「取得不可・フック全文参照」] |
| 投稿テーマ | [1行で：例「フリーター→正社員 体験談」] |
| 投稿型 | [Type-A〜F or 独自型] |
| フック（冒頭1行） | [投稿の冒頭1〜2行を全文コピー] |
| CTA | [あり・なし／フレーズ／誘導先] |
| いいね数 | |
| コメント数 | |
| リポスト/保存数 | |

**保存される理由（仮説）**
1.
2.

**真似できる要素**
- フック構造：
- 本文構成：
- CTA方法：
- その他：

**れんへの転用案**
- 転用フック：
- 転用型：
- 転用先：threads/ideas.md（記入日：）

**knowledge/post_patterns.md への反映**
- 対応Type：Type-[A〜F]
- バズ観測カウント更新：[する/しない（基準未満のため）]
```

---

## 蓄積ログ

（発見次第ここに追記する）

---

## Type別バズカウンター（weekly.md で週次更新）

competitive_patterns.md に週次集計するための中間集計テーブル。

| Type | パターン名 | 今週バズ観測数 | 累計バズ観測数 | 優先度（post_patterns.md） |
|------|---------|------------|------------|------------------------|
| A | 問題提起型 | 0 | 0 | ★ |
| B | Q&A型 | 0 | 0 | ★ |
| C | Before→After型 | 0 | 0 | ★ |
| D | ランキング型 | 0 | 0 | ★ |
| E | コメント誘導型 | 0 | 0 | ★ |
| F | ストーリー型 | 0 | 0 | ★ |

> **★★★ 昇格ライン：累計バズ観測数が3以上になったら `knowledge/post_patterns.md` の優先度を ★★★ に更新する**

---

## プラットフォーム別・今週の勝ち投稿サマリー

（毎週月曜の weekly.md タスク4 で記入する）

```
## YYYY年MM月 第__週 勝ち投稿サマリー

■ 今週の記録件数：___本（Threads:__ / X:__ / TikTok:__ / Instagram:__ / YouTube:__）

■ 最多バズType：Type-[A〜F]（___件）

■ 今週のトップフック（いいね・再生数1位）
  → [フック全文]
  → 感情タイプ：[共感型/数字型/逆説型/問いかけ型/情報開示型]

■ 今週のトップCTA
  → [CTAフレーズ]
  → 形式：[プロフィール誘導/リプライ誘導/保存誘導]

■ knowledge/post_patterns.md の更新事項
  → [更新した内容・優先度変更があればここに記録]
```

---

## 連携ファイル

```
インプット：
  research/daily_research.md  ← 毎朝の記録指示

アウトプット：
  analysis/competitive_patterns.md ← 週次分析の原データ
  knowledge/post_patterns.md       ← Type別優先度の根拠データ
  threads/ideas.md                 ← 転用アイデアの追加先
  research/hooks_archive.md        ← フック転用ストックの補充先
```

---

## TODO

- [ ] 最初の10件を記録して「バズる共通点の仮説」を立てる
- [ ] Type別バズカウンターが3以上になったら即座に post_patterns.md を更新する
- [ ] 月次でプラットフォーム横断の「バズ構造比較」を competitive_patterns.md に記録する
