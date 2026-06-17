# daily_research.md — 毎日のSNSリサーチ手順

毎日20〜25分で5プラットフォームを横断リサーチし、
その結果を research/ 配下に蓄積して REN OS 全体に学習させる。
リサーチ対象アカウントは **research/competitor_list.md** を参照する。

---

## リサーチの目的

```
市場（SNS）で何がバズっているか
→ 悩みの言葉・フック・構成を収集
→ 投稿生成に反映
→ 投稿 → 分析 → 改善 → 次の市場リサーチ

このループを毎日まわすことが目的。
```

---

## 実施タイミング

| タイミング | 所要時間 | 内容 |
|----------|---------|------|
| 毎朝 08:30（投稿前） | 20〜25分 | 5プラットフォームを横断チェック（competitor_list.md を開いて実施） |
| 毎晩 21:00（投稿後） | 5分 | 当日の自分の投稿コメントを確認 |

---

## 毎朝のリサーチ手順（20〜25分）

> **事前準備：** `research/competitor_list.md` を開いておく。
> 各ステップで「確認頻度：毎日」のアカウントを最優先に確認する。

### Step1：Threads（6分）

```
① competitor_list.md の Threads欄（TH-01〜05）を確認する
   → 確認頻度「毎日」のアカウント（TH-01・TH-02）を最優先に開く
   → 直近24時間の投稿を全件スクロールする

② キーワード検索で市場全体を確認する
   → 検索ワード：「第二新卒」「フリーター 転職」「転職 怖い」「正社員になりたい」
   → 上位表示されている投稿（いいね50以上）を確認する

③ 記録する：
   □ バズ投稿（いいね50以上）→ viral_archive.md
   □ 伸びたフック1行目 → hooks_archive.md
   □ コメント欄の質問・悩み → comment_analysis.md
   □ 気になったトレンドワード → trend.md
   □ competitor_list.md の該当アカウントの「最終確認日」を更新する
```

### Step2：X（Twitter）（4分）

```
① competitor_list.md の X欄（X-01〜03）の確認頻度に従って確認する

② トレンドを確認する（「もっと見る」→ トレンド一覧）
   → 転職・就活・第二新卒・フリーターのワードが入っていないか確認

③ キーワード検索する
   → 「転職 怖い」「第二新卒 不安」「フリーター 正社員」
   → 最新タブで過去24時間の投稿を見る

④ 記録する：
   □ リポスト・いいねが多い投稿 → viral_archive.md（X版）
   □ 伸びたフック → hooks_archive.md（X版）
   □ ユーザーの生の悩みコメント → comment_analysis.md
   □ トレンドワード → trend.md
```

### Step3：TikTok（5分）

```
① competitor_list.md の TikTok欄（TK-01〜02）の確認頻度に従って確認する
   → 対象アカウントの直近投稿を確認する

② ハッシュタグ検索でバズ動画を確認する
   → 「転職」「第二新卒」「フリーター」のハッシュタグ検索
   → 再生数1万以上の動画の「冒頭3秒」「構成」「CTA」を確認する

③ 記録する：
   □ バズ動画の冒頭フレーズ（冒頭3秒）→ hooks_archive.md（TikTok版）
   □ 構成パターン（問題提起→解決→CTA等）→ save_patterns.md
   □ コメント欄の悩みワード → comment_analysis.md
```

### Step4：Instagram（4分）

```
① competitor_list.md の Instagram欄（IG-01〜02）の確認頻度に従って確認する
   → リール・カルーセルの最新投稿を確認する

② ハッシュタグ検索で市場全体を確認する
   → #転職 #第二新卒 #フリーター転職 #転職活動

③ 記録する：
   □ 保存されやすい構成パターン → save_patterns.md
   □ コメントの質問内容 → comment_analysis.md
   □ バズ投稿（いいね500以上・保存100以上）→ viral_archive.md
```

### Step5：YouTube Shorts（4分）

```
① competitor_list.md の YouTube Shorts欄（YT-01〜02）の確認頻度に従って確認する
   → 対象チャンネルの直近Shortsを確認する

② キーワード検索でバズShortsを確認する
   → 検索ワード：「転職 第二新卒」「フリーター 正社員」「転職 面接」
   → フィルタ：「動画」「今月」で絞り込む

③ 確認ポイント：
   □ サムネイルの文字（フック）→ hooks_archive.md（YouTube Shorts版）
   □ 冒頭5秒のセリフ・テキスト → hooks_archive.md
   □ 動画の構成（問題提起→解説→CTA）→ save_patterns.md
   □ コメント欄の悩みワード → comment_analysis.md

④ 記録する：
   □ 再生数10万以上のShortsがあれば → viral_archive.md に記録
   □ competitor_list.md の「最終確認日」を更新する
```

---

## 【必須】勝ち投稿の保存（毎朝・5分）

> Step1〜5 のリサーチ後、必ずこのステップを実行する。
> **最低3本 / 日** の勝ち投稿を `research/winning_posts.md` に記録する。

```
① 今朝のリサーチで「いちばん伸びていた投稿」を各プラットフォームから1本ずつ選ぶ
   → 選定基準：Threads（いいね50以上）/ X（リポスト10以上）/ TikTok（再生1万以上）
   　　　　　　Instagram（いいね500以上 or 保存100以上）/ YouTube Shorts（再生10万以上）

② research/winning_posts.md のテンプレートをコピーして記録する
   必須項目：投稿URL（取れない場合はフック全文）・投稿型・フック・CTA・いいね数・コメント数
   必須記入：「保存される理由」2点・「真似できる要素」（フック構造/本文構成/CTA方法）

③ 同じType（A〜F）の投稿が今週2本目以上になった場合：
   → winning_posts.md の「Type別バズカウンター」を更新する
   → 累計3本に達したら knowledge/post_patterns.md の該当Typeを ★★★ に昇格させる

④ 特に優秀なフックがあれば research/hooks_archive.md の転用ストックにも追記する
```

**週次（月曜）に実施：**
```
□ winning_posts.md の今週記録を集計する
□ analysis/competitive_patterns.md の週次レポートテンプレートを記入する
□ knowledge/post_patterns.md のパフォーマンスサマリーを更新する
□ threads/ideas.md に転用アイデアを追加する
```

---

## 毎晩のリサーチ手順（5分）

```
① 当日の自分の投稿（5本）のコメント・返信を確認する
   □ 質問・悩みが来ていたら comment_analysis.md に追記する
   □ 特定のフックに反応が多かった場合 hooks_archive.md の評価欄を更新する
   □ いいね・リポストが平均より多い投稿がある場合 viral_archive.md に記録する
```

---

## 見るべき指標（プラットフォーム別）

### Threads
| 指標 | 判断基準 | 記録先 |
|-----|---------|-------|
| いいね数 | 50以上→バズ候補 | viral_archive.md |
| リプライ数 | 10以上→エンゲージメント高 | viral_archive.md |
| 引用・リポスト | あり→拡散力あり | viral_archive.md |
| プロフィール遷移 | 計測できないため間接推定 | - |

### X
| 指標 | 判断基準 | 記録先 |
|-----|---------|-------|
| リポスト数 | 10以上→バズ候補 | viral_archive.md |
| いいね数 | 100以上→バズ候補 | viral_archive.md |
| 返信数 | 20以上→議論系バズ | comment_analysis.md |

### TikTok
| 指標 | 判断基準 | 記録先 |
|-----|---------|-------|
| 再生数 | 1万以上→構成を参考にする | save_patterns.md |
| いいね数 | 1,000以上→バズ候補 | viral_archive.md |
| コメント数 | 100以上→悩みリサーチに使う | comment_analysis.md |

### Instagram
| 指標 | 判断基準 | 記録先 |
|-----|---------|-------|
| 保存数 | 100以上→構成を参考にする | save_patterns.md |
| いいね数 | 500以上→バズ候補 | viral_archive.md |
| コメント数 | 30以上→悩みリサーチに使う | comment_analysis.md |

---

## 保存方法

```
リサーチで発見したものの保存先：

競合アカウント管理    → research/competitor_list.md（マスターリスト）
競合バズ投稿の記録    → research/competitor_tracker.md（観測ログ）
バズ投稿全体分析      → research/viral_archive.md
フック1行目           → research/hooks_archive.md
コメント・悩み        → research/comment_analysis.md
トレンドワード        → research/trend.md
保存パターン          → research/save_patterns.md

週次まとめ後の反映先：
knowledge/hooks.md         ← 使えるフックを追加
threads/ideas.md           ← ネタを追加
knowledge/pain_points.md   ← 新しい悩みを追加
threads/viral_patterns.md  ← バズパターンを更新
```

---

## research/ → 各フォルダへの反映ルール

| 反映タイミング | 反映内容 | 反映先 |
|-------------|---------|-------|
| 毎日（気づきがある日） | 新フック・新悩みワード | hooks_archive.md / comment_analysis.md |
| 週次（月曜） | 週間バズパターン・トップフック | knowledge/hooks.md / threads/viral_patterns.md |
| 月次 | 月次トレンドサマリー | knowledge/market.md（TODO） / trend.md |

---

## TODO

- [ ] competitor_list.md に実際のアカウントを記入してリサーチを開始する
- [ ] Threadsの検索キーワードをブックマークし、毎朝1タップで開けるようにする
- [ ] TikTokの転職系ハッシュタグページをブックマークする
- [ ] Instagramのハッシュタグページをブックマークする
- [ ] YouTube Shortsの検索フィルタ（動画・今月）の操作手順に慣れる
- [ ] 週次でresearch/の蓄積データをknowledge/に反映する習慣を作る
- [ ] リサーチ所要時間が25分を超えるようになったら手順を簡略化する
