# master_flow.md — REN OS マスターフロー

REN OS 全体の実行ループ定義。このループが毎日・毎週・毎月まわり続けることで、
自動的に改善しながら収益が積み上がるシステムになる。

---

## REN OS 全体ループ（v3.1）

```
┌──────────────────────────────────────────────────────────────────┐
│                      REN OS LOOP v3.1                            │
│                                                                  │
│  ①market（SNS市場リサーチ）← research/ フォルダ                 │
│     ↓  毎朝08:30・25〜30分                                       │
│  ①-B 勝ち投稿保存                                               │
│     ↓  伸びた投稿を最低3本 → research/winning_posts.md に記録   │
│  ①-C 共通点抽出                                                 │
│     ↓  Type別バズカウンター更新 → knowledge/post_patterns.md へ │
│  ②knowledge更新                                                  │
│     ↓  post_patterns.md の優先度を反映 → 投稿型の優先順位を決定 │
│  ③投稿生成（generate_posts）                                     │
│     ↓  post_patterns.md を最初に読み込み・★★★型を優先生成      │
│  ④Threads投稿（自動・1日5本）                                    │
│     ↓                                                            │
│  ⑤LINE登録                                                       │
│     ↓                                                            │
│  ⑥フォーム回答                                                   │
│     ↓                                                            │
│  ⑦個別相談                                                       │
│     ↓                                                            │
│  ⑧ASP案件紹介・成約                                              │
│     ↓                                                            │
│  ⑨analysis（分析）                                               │
│     ↓  competitive_patterns.md で競合パターン週次分析            │
│  ⑩improvement（改善）                                            │
│     ↓  post_patterns.md を更新 → 次のループの生成精度が上がる   │
│  ①market（市場）→ ①-B へ戻る（永久ループ）                     │
└──────────────────────────────────────────────────────────────────┘
```

### v3.1 追加フロー（勝ち投稿学習サイクル）

```
【毎日】
市場調査（research/daily_research.md）
  ↓
勝ち投稿保存（research/winning_posts.md に最低3本）
  ↓
共通点抽出（Type別バズカウンター更新）
  ↓
knowledge更新（post_patterns.md の優先度反映）
  ↓
投稿生成（★★★型を優先・競合3回バズで自動昇格）

【毎週（月曜）】
competitive_patterns.md で4軸ランキング集計
  ↓
knowledge/post_patterns.md の優先度を確定更新
  ↓
generate_posts.md の来週生成方針を更新
```

---

## 各ステップの詳細

### ① market（SNS市場リサーチ）

**役割：** 毎朝5プラットフォームをリサーチし、最新の「何がバズっているか・何が悩まれているか」を収集する。

```
実施：毎朝08:30・25〜30分（automation/daily.md タスク0）
5プラットフォーム：Threads / X / TikTok / Instagram / YouTube Shorts
```

| 収集内容 | 保存先 |
|--------|-------|
| 勝ち投稿（最低3本/日） | research/winning_posts.md ← v3.1追加 |
| バズ投稿の構成・フック | research/viral_archive.md |
| 伸びたフック1行目 | research/hooks_archive.md |
| コメントの悩み・質問 | research/comment_analysis.md |
| トレンドワード | research/trend.md |
| 競合アカウントの動き | research/competitor_tracker.md |
| 保存される投稿の構造 | research/save_patterns.md |

**勝ち投稿からの学習フロー（v3.1追加）：**

```
winning_posts.md に3本記録
  ↓
Type別バズカウンターを更新
  ↓
累計3以上 → knowledge/post_patterns.md を ★★★ に昇格
  ↓
generate_posts.md の次回生成で ★★★ 型を必ず2本以上使う
```

**週次反映：** research/ + competitive_patterns.md の分析を knowledge/ / threads/ に転記する（automation/weekly.md タスク4）

---

### ① knowledge（知識ベース）

**役割：** REN OS 全体の「脳」。投稿・LINE・ブログ・ASP全てはここを起点にする。

| ファイル | 内容 |
|--------|-----|
| knowledge/persona.md | れんのキャラクター・話し方・価値観 |
| knowledge/target.md | ターゲット詳細（18〜34歳・第二新卒等） |
| knowledge/value_proposition.md | れんの提供価値・他との差別化 |
| knowledge/pain_points.md | ターゲットの悩み・不安リスト |
| knowledge/success_stories.md | 転職成功事例（体験談の素材） |
| knowledge/market.md | 転職市場の最新データ |

**更新タイミング：** 月次改善後・新しい体験談が生まれたとき

---

### ② 投稿生成（generate_posts）

**役割：** knowledge/ を読み込んで、Threads投稿ネタをまとめて生成する。

```
実行タイミング：月1回（翌月分20〜30本）
使用ツール：Claude（automation/generate_posts.md のプロンプト使用）
出力先：posts.csv
```

**生成ルール（automation/generate_posts.md 参照）：**
- 体験談50% / ノウハウ30% / 共感20%
- テンプレート T01〜T10 を均等に使う
- 投稿20本中 CTA（LINE誘導）は2本のみ
- knowledge/ + analysis/viral_analysis.md + threads/ng_patterns.md を必ず読む

---

### ③ Threads投稿（自動）

**役割：** posts.csv から毎日5本を自動投稿する。Threads経由でフォロワーを増やし、LINEへ誘導する。

```
実行：Windows Task Scheduler → python main.py --execute
時間：07:00 / 10:00 / 13:00 / 18:00 / 20:00 JST
social_set_id：310888
```

**ステップ：**
1. Task Scheduler が `main.py --execute` を起動
2. posts.csv から未投稿のネタを取得
3. Typefully API v2 でスケジュール投稿
4. 投稿済みフラグを posts.csv に記録

---

### ④ LINE登録

**役割：** Threads投稿を見たフォロワーが、CTAを見てLINEに登録する。

```
登録経路：Threadsプロフィール / CTA投稿（週1〜2回） / ブログ記事
登録後：ステップ配信（Day0〜7）が自動で流れる（TODO：設定後）
```

**ファイル：** line/greeting.md / line/step_messages.md / line/richmenu.md

---

### ⑤ フォーム回答

**役割：** LINE登録者にフォームを案内し、ヒアリングを効率化する。

```
案内タイミング：LINE登録直後（ステップ配信Day1）
フォームURL：TODO（作成後に設定）
目標完了率：55%以上
```

**ファイル：** forms/questions.md / forms/logic.md / forms/conversion.md

---

### ⑥ 個別相談

**役割：** フォーム回答者を相談へ誘導し、状況をヒアリングする（30〜60分）。

```
形式：TODO（テキスト/音声/ビデオ等は検討中）
目標相談予約率：フォーム完了者の50%
```

**ファイル：** line/consultation_flow.md / asp/offer_flow.md

---

### ⑦ ASP案件紹介・成約

**役割：** 相談後に最適なエージェントを提案し、登録・面談へ誘導してASP成約を得る。

```
主要案件：第二新卒エージェントneo・就職カレッジ（稼働中）
        UZUZ・キャリアスタート（登録予定）
目標登録率：相談者の60%
```

**ファイル：** asp/selection_rules.md / asp/copywriting.md / asp/offer_flow.md

---

### ⑧ analysis（分析）

**役割：** 各チャネルの数値を集計し、どこが伸びていて・どこが詰まっているかを把握する。競合パターン分析も毎週実施する。

```
週次（月曜・45分）：
- Threads：フォロワー・エンゲージメント・バズ投稿
- LINE：登録数・ブロック率・フォーム誘導
- フォーム：完了率・離脱箇所
- ASP：承認・否認
- ブログ：PV・順位変動
- 競合パターン分析（v3.1追加）：
    winning_posts.md を集計 → competitive_patterns.md に週次レポートを記入
    → knowledge/post_patterns.md の優先度を更新

月次（最終月曜・90分）：
- 全チャネルのKPI集計
- ファネル転換率の全体把握
- 改善優先度の決定
- competitive_patterns.md の月次サマリーを記入
```

**ファイル：** analysis/dashboard.md / analysis/weekly_review.md / analysis/monthly_review.md / analysis/competitive_patterns.md（v3.1追加）

---

### ⑨ improvement（改善）

**役割：** 分析で見つかった課題を、対応するフォルダに反映する。

```
改善の流れ：
analysis → どのチャネルが弱いか特定
→ 対応フォルダのファイルを更新（threads/line/forms/blog/asp）
→ 翌週・翌月の投稿・返信・記事に反映
```

**ファイル：** automation/improve.md / 各フォルダの improvement.md

---

### ① knowledge更新（ループへ戻る）

**役割：** 相談・成功事例・バズパターンから新しい知識を knowledge/ に追加し、次のループの質を上げる。

```
更新タイミング：月次改善後（最終月曜）
更新内容：
- 新しい成功事例 → knowledge/success_stories.md
- バズしたフック・型 → threads/hooks.md / templates.md
- フォームで多かった悩み → knowledge/pain_points.md
- 否認原因 → asp/selection_rules.md / knowledge/market.md
```

---

## ループの全体像（時間軸）

```
【毎日】
07:00 → 投稿①自動
10:00 → 投稿②自動
13:00 → 投稿③自動 ＋ フォーム確認・返信（手動5分）
18:00 → 投稿④自動
20:00 → 投稿⑤自動 ＋ コメント返信（手動10分）
09:00 → LINE返信（手動15分）
           ↓
     → 相談が入れば → ASP紹介 → tracking.md記録

【毎週（月曜）】
09:00〜11:30 → 分析・改善・補充の週次ルーティン

【毎月（最終月曜）】
10:00〜14:30 → 月次分析・改善・翌月準備のルーティン

【ループのスピード】
投稿改善ループ：1週間
LINE/フォームループ：2週間
ASPループ：1ヶ月
ブログSEOループ：3ヶ月
```

---

## ループの健全性チェック

以下の状態が続いていれば、REN OS は正常に稼働している。

```
✅ 毎日5本の投稿が自動投稿されている
✅ 毎朝 winning_posts.md に3本以上の勝ち投稿が記録されている（v3.1追加）
✅ 週次で new_posts.md のバズカウンターが更新されている（v3.1追加）
✅ 週次で新規LINE登録がある
✅ フォーム完了率が55%以上
✅ 月次でASP承認が1件以上
✅ ブログ記事が月3〜4本公開されている
✅ posts.csv に常に10本以上のストックがある
✅ 月次レポートが reports.md に記録されている
```

いずれかが ✅ でない場合は `analysis/alerts.md` を確認し、対応するアクションを実施する。

---

## REN OS フォルダ構成

```
threads-os/
├── AGENTS.md                    ← REN OS v2.0 ルール定義
├── posts.csv                    ← 投稿ネタストック
├── main.py                      ← 自動投稿スクリプト
│
├── research/                    ← ①市場リサーチ（ループの最上流）
│   ├── daily_research.md        ← 毎日の調査手順・指標・保存方法
│   ├── winning_posts.md         ← 勝ち投稿DB・Typeバズカウンター（v3.1追加）
│   ├── competitor_tracker.md    ← 競合アカウント管理・バズ投稿記録
│   ├── competitor_list.md       ← 競合アカウントマスターリスト
│   ├── viral_archive.md         ← バズ投稿DB（5プラットフォーム）
│   ├── comment_analysis.md      ← コメント悩み抽出・ネタ化
│   ├── trend.md                 ← トレンド追跡（転職・SNSアルゴリズム等）
│   ├── hooks_archive.md         ← 伸びたフック1行目アーカイブ
│   └── save_patterns.md         ← 保存される投稿の特徴・構造
│
├── knowledge/                   ← ②知識ベース（research/から更新される）
│   ├── post_patterns.md         ← 勝ち投稿テンプレートDB・優先度管理（v3.1追加）
├── threads/                     ← ③投稿生成・管理
├── line/                        ← ⑤LINE運用
├── forms/                       ← ⑥フォーム設計
├── blog/                        ← 補助集客チャネル
├── asp/                         ← ⑧ASP案件管理
├── analysis/                    ← ⑨分析（結果をresearch/に還流）
│   ├── competitive_patterns.md  ← 競合パターン週次分析・4軸ランキング（v3.1追加）
└── automation/                  ← ⑩改善＋全体の自動運用定義
    ├── master_flow.md           ← このファイル
    ├── scheduler.md             ← 実行スケジュール
    ├── checklist.md             ← 運用漏れ防止
    ├── reports.md               ← レポート蓄積
    ├── daily.md                 ← 毎日タスク
    ├── weekly.md                ← 毎週タスク
    ├── monthly.md               ← 毎月タスク
    ├── generate_posts.md        ← 投稿生成手順
    ├── analyze.md               ← 分析実行手順
    ├── improve.md               ← 改善実行手順
    ├── line_tasks.md            ← LINE運用タスク
    ├── blog_tasks.md            ← ブログ運用タスク
    ├── asp_tasks.md             ← ASP運用タスク
    ├── competitor_watch.md      ← 競合監視
    └── todo.md                  ← 優先度別タスク管理
```
