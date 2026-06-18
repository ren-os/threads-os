# 週次レポート — （自動更新）

> 自動生成: `scripts/ga4_report.py`  |  測定ID: G-R3JPL9E7TM
> このファイルは毎週月曜朝 GitHub Actions が上書きします。手動で実行する場合：
> ```bash
> python scripts/ga4_report.py weekly
> python scripts/ga4_report.py weekly --end-date 20260618  # 特定の週末日を指定
> ```

---

## 週間サマリー

（スクリプト実行後に自動入力されます）

| 指標 | 週合計 | 目標 | 状態 |
|-----|------|-----|-----|
| PV | — | — | — |
| 診断開始数 | — | — | — |
| 診断開始率 | —% | 40%以上 | — |
| 診断完了数 | — | — | — |
| 診断完了率 | —% | 70%以上 | — |
| CTAクリック数 | — | — | — |
| CTAクリック率 | —% | 15%以上 | — |

---

## 日別トレンド

| 日付 | PV | 診断開始 | 開始率 | 診断完了 | 完了率 | CTAクリック | CTA率 |
|-----|---|--------|------|--------|------|-----------|-----|
| — | — | — | — | — | — | — | — |

---

## utm_campaign 別（週次）

| utm_campaign | ラベル | PV | 診断開始 | 診断完了 | CTAクリック | 完了率 |
|-------------|-------|---|--------|--------|-----------|------|
| `career_diagnosis_interview` | 面接官シリーズ | — | — | — | — | — |
| `career_diagnosis_jinjika` | 元人事シリーズ | — | — | — | — | — |
| `career_diagnosis_black` | ブラック企業シリーズ | — | — | — | — | — |
| `career_diagnosis_daini` | 第二新卒シリーズ | — | — | — | — | — |
| `career_diagnosis_freeter` | フリーターシリーズ | — | — | — | — | — |

---

## Threads投稿シリーズ 効果ランキング（診断完了数順）

| ランク | 投稿シリーズ | utm_campaign | 診断完了数 | CTAクリック数 | CTA率 |
|------|-----------|-------------|---------|------------|------|
| 1 | — | — | — | — | — |

---

## 来週のアクション

| 優先度 | アクション | 根拠 |
|------|---------|-----|
| 高 | （数値を見て記入） | — |
| 中 | — | — |

---

## 週次チェックリスト

毎週月曜日に確認する：

- [ ] 週間PV数の変化（増減率）
- [ ] 診断開始率 → 目標40%以上
- [ ] 診断完了率 → 目標70%以上
- [ ] CTAクリック率 → 目標15%以上
- [ ] 最も診断完了を生んだThreads投稿シリーズを確認
- [ ] 流入が0の utm_campaign → Threads投稿にUTMリンクが設定されているか確認
- [ ] 前週比で大きく下がった指標の原因を特定

---

## Threads投稿へのUTMリンク設定方法

各投稿に以下のURLを貼る（シリーズに応じて utm_campaign を変える）：

```
https://ren-os.github.io/threads-os/career-diagnosis/?utm_source=threads&utm_medium=post&utm_campaign=career_diagnosis_interview
```

| 投稿シリーズ | utm_campaign の値 |
|-----------|----------------|
| 面接官シリーズ | `career_diagnosis_interview` |
| 元人事シリーズ | `career_diagnosis_jinjika` |
| ブラック企業シリーズ | `career_diagnosis_black` |
| 第二新卒シリーズ | `career_diagnosis_daini` |
| フリーターシリーズ | `career_diagnosis_freeter` |

### 個別投稿を追跡したい場合

`utm_content` に日付＋番号を入れると投稿単位で追跡できる：

```
?utm_source=threads&utm_medium=post&utm_campaign=career_diagnosis_daini&utm_content=20260618_1
```

GA4 の探索レポートで `sessionCampaignName` + `sessionManualAdContent` をディメンションに追加すると投稿単位の比較が可能。

---

## 改善アクション指針

| 指標が低い場合 | 原因仮説 | アクション |
|------------|--------|---------|
| 診断開始率 < 40% | トップのメッセージがズレている | コピーABテスト・ビジュアル変更 |
| 診断完了率 < 70% | 途中の質問でつまずいている | GA4でどの質問番号で離脱が多いか確認（question_abandonイベントを追加検討） |
| CTAクリック率 < 15% | 結果画面の信頼感が低い | CTA文言・ボタンデザイン・「強引な勧誘なし」の訴求強化 |
| campaign別に偏りがある | 特定シリーズだけ流入がない | そのシリーズの投稿本数・フック文を見直す |
