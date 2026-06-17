# generate_posts.md — 投稿生成フロー

Threads投稿を生成するときに必ず実行するフロー。
このファイルを読んでからClaude（またはれん自身）が投稿を生成する。

---

## 生成の基本ルール

- 1回の生成で20本以上を生成する（4日分）
- 生成前に必ず参照ファイルを読み込む（読み飛ばし禁止）
- 重複チェックを必ず通す
- 生成後は threads/posted_log.md にセット番号を記録する

---

## Step1：必須読み込みファイル（生成前に必ず確認）

以下を順番に読み込む。読み込まずに生成した投稿は使用しない。
**post_patterns → research/ → knowledge/ → threads/ → analysis/ の順に読む。**

### knowledge/post_patterns.md （★最優先・最初に読む）

```
□ knowledge/post_patterns.md
  → パフォーマンスサマリーを確認する
  → ★★★（最優先）の Type を特定する
    → ★★★ Type は今回の生成に必ず2本以上含める
  → ★★（高優先）の Type を確認する
    → ★★ Type は今回の生成に1本以上含める
  → 競合で同じ構成が3回以上バズっていたパターンは
    → そのTypeの優先順位を1段階上げて生成する

【生成前の Type 優先度確認チェック】
  最優先（★★★）Type：___（必ず2本以上）
  高優先（★★）Type：___（1本以上）
  通常（★）Type：___（バランスで使用）
  今回の生成で避けるType（3週連続低パフォーマンス等）：___
```

### research/ （最新市場情報・最優先）

```
□ research/trend.md
  → 今週・今月のトレンドワードを確認する
  → 季節性ネタが仕込める時期かを確認する
  → トレンドに合ったテーマを今回の生成に1〜2本反映する

□ research/hooks_archive.md
  → 「れんが使えるフック転用ストック」を確認する
  → 感情タイプ別の今週推奨フック型を確認する
  → knowledge/hooks.md の未使用フックより優先的に参照する

□ research/viral_archive.md
  → 直近2週間のバズ投稿を確認する
  → バズっている型・ジャンル・フック構造を今回の生成に反映する

□ research/save_patterns.md
  → 今週の推奨保存型を確認する
  → 生成20本中30〜40%（6〜8本）は保存狙い型にする

□ research/comment_analysis.md
  → 直近1週間のコメントから「よく出た悩みワード」を確認する
  → その悩みをフック・本文・テーマに反映する

□ research/competitor_tracker.md
  → 競合が最近バズらせた型・テーマを確認する
  → 同じテーマを独自の視点で書けないか確認する

□ research/winning_posts.md
  → 直近1週間の勝ち投稿ログを確認する
  → Type別バズカウンターで「3以上」のTypeを確認する
    → 3以上のTypeは post_patterns.md で ★★★ になっているはず（整合確認）
  → トップフック・トップCTAを今回の生成に反映する
```

### knowledge/ （静的知識ベース）

```
□ knowledge/offer.md
  → LINE_URL を確認する（投稿本文には貼らない）
  → LINE導線ルールを確認する：
     ・通常投稿にURL直貼り禁止
     ・CTA標準フレーズ「無料相談はプロフィールのリンクから👇」で統一
     ・プロフィールにLINEリンク設置済みを前提とする

□ knowledge/brand.md
  → ブランド名「れん」・トーン・NG表現を確認する

□ knowledge/target.md
  → ターゲット（あおい24歳/けんた26歳/さくら23歳）を確認する

□ knowledge/content_pillars.md
  → 今月の優先テーマと比率（体験談50%/ノウハウ30%/共感20%）を確認する

□ knowledge/posting_rules.md
  → 文字数（150〜350字）・NGワード・CTA比率・LINE導線ルールを確認する

□ knowledge/faq.md
  → よくある質問をネタに使えるか確認する

□ knowledge/objections.md
  → よくある不安・反論をネタに使えるか確認する
```

### threads/ （動的運用データ）

```
□ threads/hooks.md
  → 「使用済みフック」を確認する（重複を避ける）
  → 「未使用ストック」から今回使うフックを選ぶ

□ threads/viral_patterns.md
  → 高パフォーマンスパターン（優先順位TOP3）を確認する
  → 今回の生成でどのパターンを使うか決める

□ threads/posted_log.md
  → 直近20本の投稿テーマ・型・ジャンルを確認する（ネタ重複を防ぐ）
  → 「使用済みテーマ一覧」に記載されたネタは使わない

□ threads/post_templates.md
  → 「次の優先型」（T02/T04/T08/T09等）を確認する
  → 最後に使った型と同じ型を連続させない

□ threads/ideas.md
  → 「優先度：高」のネタリストから今回使うネタを選ぶ

□ threads/improvement.md
  → 「次回反映事項」を確認し、今回の生成に反映する

□ threads/ab_test.md
  → 進行中のA/Bテスト仕様（フック型・CTA文・投稿時間）を確認する
  → テスト中の仕様に沿って生成する

□ threads/kpi.md
  → 現在のKPI状況を確認し、弱い指標に対応する型を増やす
```

### analysis/ （改善インサイト）

```
□ analysis/viral_analysis.md
  → 先週のバズ投稿・沈没投稿のパターンを確認する
  → 沈没投稿と同じフック・型・ジャンルは避ける

□ analysis/content_analysis.md
  → 型別・フック別の最新パフォーマンスを確認する
  → 低パフォーマンスの型は今回の生成比率を下げる
```

---

## Step2：生成条件の確認

読み込んだファイルをもとに、今回の生成条件を設定する。

```
【今回の生成条件シート】

■ 生成本数：20本（最低20本・理想25本）

■ ジャンル比率（knowledge/content_pillars.md 参照）
- 体験談（ストーリー）：XX本（50%）
- ノウハウ：XX本（20%）
- 知らないと損する：XX本（10%）
- 共感：XX本（20%）
- CTA含み：2本以内

■ 今回の優先型（threads/post_templates.md 参照）
- 使う型：T__, T__, T__
- 避ける型（低パフォーマンス or 直近多用）：T__

■ 今回のフック方針（threads/hooks.md 参照）
- 使うフックタイプ：
- 避けるフック（使用済み or 低パフォーマンス）：

■ 今回のCTA方針（threads/cta.md 参照）
- ローテーション順番：

■ A/Bテスト仕様（threads/ab_test.md 参照）
- テスト中の変数：
```

---

## Step3：投稿生成

生成条件に沿って20本以上の投稿を生成する。

### 生成プロンプト（Claude用）

```
以下のルールに沿って、Threads投稿を20本生成してください。

【ターゲット】
knowledge/target.md のペルソナ（あおい/けんた/さくら）に刺さる内容

【文字数】
150〜350文字

【比率】
体験談50% / ノウハウ30% / 共感20%
CTA含みは20本中2本以内

【投稿Type優先度（knowledge/post_patterns.md より）← v3.1追加・最重要】
- ★★★ Type（最優先）：___
  → 今回の生成に必ず2本以上含める
  → 競合で3回以上同じ構成がバズっていたパターン。最優先で使う。
- ★★ Type（高優先）：___
  → 今回の生成に1本以上含める
- ★ Type（通常）：残り本数でバランスよく使う
- 競合で同じ構成が3回以上バズっていたTypeは優先順位を1段階上げて使う

【market反映（research/ より）】
- research/winning_posts.md のトップフック・トップTypeを今回の生成に反映する
- research/trend.md のトレンドワードをフック・テーマに1〜2本反映する
- research/hooks_archive.md の「転用ストック」から今回使うフックを選ぶ
- research/viral_archive.md のバズ構造を今回の生成に取り込む
- research/comment_analysis.md の悩みワードをフック・本文に使う

【LINE導線ルール（必須）】
- 通常投稿の本文にLINE URLを絶対に入れない
- CTAフレーズは「無料相談はプロフィールのリンクから👇」で統一する
- CTA投稿は20本中2本以内に抑える
- バリエーションは前置き＋標準フレーズの組み合わせのみ許可
  例：「同じ状況の方は、無料相談はプロフィールのリンクから👇」

【避けること】
- threads/posted_log.md に記載された使用済みネタ
- threads/hooks.md の使用済みフック
- knowledge/posting_rules.md のNGワード
- LINE URLの本文直貼り（knowledge/offer.md の LINE_URL 参照）
- research/competitor_tracker.md のバズ投稿のフックをそのままコピーする
- research/winning_posts.md の「真似できる要素」を構造ごとコピーする（構造は転用OK・文章はNG）

【今回使う優先型・フック】
（Step2の生成条件シートを貼り付ける）

【出力形式】
id, content, category, type（Type-A〜F）, created_at の形式でCSV出力
```

---

## Step4：重複チェック

```
チェック手順：
1. 生成した投稿テキストのMD5ハッシュを取得する
2. posted_log.md の過去投稿と類似度（0.85以上）をチェックする
3. 重複する投稿は除外し、代替投稿を生成する
4. python main.py --dry-run で最終確認する
```

---

## Step5：posts.csv への追加・記録

```
実行手順：
1. チェック済みの投稿を posts.csv に追記する
2. threads/posted_log.md に新セット番号と投稿一覧を記録する
3. threads/ideas.md の「使用済み」欄を更新する
4. threads/hooks.md の「使用済みフックセット」を更新する
```

---

## 生成頻度

| 状況 | 生成タイミング |
|-----|------------|
| 通常 | 月次（monthly.md のタスク4）で20本以上生成 |
| 残数 < 10本のとき | 週次チェック時に追加生成 |
| 残数 < 5本のとき | 当日中に緊急生成（daily.md 参照） |

---

## TODO

- [ ] Claude を使った生成時はこのファイルを毎回冒頭に添付するルールを徹底する
- [ ] 将来的にClaude APIを使った自動生成を実装することを検討する
- [ ] 生成品質のチェックリストを threads/posting_checklist.md と統合する
