# 日次レポート — （自動更新）

> 自動生成: `scripts/ga4_report.py`  |  測定ID: G-R3JPL9E7TM
> このファイルは毎朝 GitHub Actions が上書きします。手動で確認したい場合は下記コマンドを実行してください。
> ```bash
> python scripts/ga4_report.py daily
> ```

---

## 確認手順（手動チェック）

### GA4 コンソールで確認する場合

1. [GA4 管理画面](https://analytics.google.com/) → プロパティ `G-R3JPL9E7TM` を開く
2. 「レポート」→「エンゲージメント」→「イベント」

### チェックすべき指標

| 指標 | GA4での場所 | 計算式 |
|-----|-----------|-------|
| PV | エンゲージメント → ページとスクリーン | — |
| 診断開始率 | イベント → `start_diagnosis` | start ÷ PV × 100 |
| 診断完了率 | イベント → `complete_diagnosis` | complete ÷ start × 100 |
| CTAクリック率 | イベント → `cta_click` | cta ÷ complete × 100 |

---

## KPI目標値

| 指標 | 目標 | 注意ライン | 危険ライン |
|-----|-----|---------|---------|
| 診断開始率 | 40%以上 ✅ | 20〜39% ⚠️ | 20%未満 🔴 |
| 診断完了率 | 70%以上 ✅ | 40〜69% ⚠️ | 40%未満 🔴 |
| CTAクリック率 | 15%以上 ✅ | 8〜14% ⚠️ | 8%未満 🔴 |

---

## utm_campaign 別パフォーマンス

（スクリプト実行後に自動入力されます）

| utm_campaign | ラベル | PV | 診断開始 | 診断完了 | CTAクリック | 完了率 |
|-------------|-------|---|--------|--------|-----------|------|
| `career_diagnosis_interview` | 面接官シリーズ | — | — | — | — | — |
| `career_diagnosis_jinjika` | 元人事シリーズ | — | — | — | — | — |
| `career_diagnosis_black` | ブラック企業シリーズ | — | — | — | — | — |
| `career_diagnosis_daini` | 第二新卒シリーズ | — | — | — | — | — |
| `career_diagnosis_freeter` | フリーターシリーズ | — | — | — | — | — |

---

## Threads投稿シリーズ別

| 投稿シリーズ | utm_campaign | 診断完了数 | CTAクリック数 |
|-----------|-------------|---------|------------|
| 面接官シリーズ | `career_diagnosis_interview` | — | — |
| 元人事シリーズ | `career_diagnosis_jinjika` | — | — |
| ブラック企業シリーズ | `career_diagnosis_black` | — | — |
| 第二新卒シリーズ | `career_diagnosis_daini` | — | — |
| フリーターシリーズ | `career_diagnosis_freeter` | — | — |

---

## セットアップ手順

スクリプトを動かすには以下の設定が必要です。

### 1. GA4 プロパティIDを確認する

GA4 管理画面 → プロパティ設定 → プロパティID（数値）をコピー

### 2. サービスアカウントを作成する

1. [Google Cloud Console](https://console.cloud.google.com/) → IAMと管理 → サービスアカウント
2. 新規作成 → JSONキーをダウンロード → `config/ga4_service_account.json` に保存
3. GA4管理画面 → プロパティアクセス管理 → サービスアカウントのメールアドレスを「閲覧者」で追加

### 3. .env に追記する

```
GA4_PROPERTY_ID=123456789
GOOGLE_APPLICATION_CREDENTIALS=config/ga4_service_account.json
```

### 4. パッケージをインストールする

```bash
pip install -r requirements.txt
```

### 5. テスト実行

```bash
python scripts/ga4_report.py daily
```

---

## 改善アクション指針

| 指標が低い場合 | 改善アクション |
|------------|------------|
| 診断開始率 < 40% | トップ画面のコピー・「無料で診断する」ボタンの視認性改善 |
| 診断完了率 < 70% | 質問文の難易度・UI のつまずき箇所を確認（どの質問で離脱しているか） |
| CTAクリック率 < 15% | 結果画面のCTAコピー・デザイン・信頼性訴求を見直す |
| Threads流入が少ない | 投稿フック文と診断LPのメッセージ一致度を確認 |
