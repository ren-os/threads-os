# threads-os — Threads自動予約システム

Typefully API v2 を使って、Threadsへの投稿を毎日自動予約するPythonスクリプトです。

---

## ディレクトリ構成

```
threads-os/
├── config/
│   └── config.yaml          # 投稿設定
├── posts/
│   ├── posts.csv            # 投稿コンテンツ（CSV形式）
│   └── posts.json           # 投稿コンテンツ（JSON形式）
├── logs/
│   ├── posted_log.csv       # 予約済み投稿ログ（自動生成）
│   └── scheduler.log        # 実行ログ（自動生成）
├── scheduler/
│   └── typefully_client.py  # Typefully APIクライアント
├── scripts/
│   └── schedule_posts.py    # メインスクリプト
├── .env                     # APIキー（gitignore推奨）
├── .env.example             # .envのテンプレート
├── requirements.txt
├── main.py                  # エントリーポイント
└── README.md
```

---

## セットアップ

### 1. Pythonの確認（3.11以上推奨）

```powershell
python --version
```

### 2. 依存パッケージのインストール

```powershell
cd threads-os
pip install -r requirements.txt
```

### 3. .envを作成

`.env.example` をコピーして `.env` を作成します。

```powershell
copy .env.example .env
```

`.env` を開いて、Typefully APIキーを入力します。

```
TYPEFULLY_API_KEY=lzraS68qdawbpqBXHoBBPpCpOxcczRRD
```

### 4. social_set_idを確認する

Typefully APIでアカウントIDを取得します。

```powershell
python -c "
import os, requests
from dotenv import load_dotenv
load_dotenv()
r = requests.get('https://api.typefully.com/v2/social-sets', headers={'Authorization': f'Bearer {os.getenv(\"TYPEFULLY_API_KEY\")}'})
import json; print(json.dumps(r.json(), indent=2, ensure_ascii=False))
"
```

出力された `id` をコピーして `config/config.yaml` の `social_set_id` に貼り付けます。

---

## config.yamlの設定

```yaml
typefully:
  social_set_id: "ここにsocial_set_idを貼る"
  platform: "threads"

posting:
  timezone: "Asia/Tokyo"
  post_count_per_day: 5
  schedule_times:
    - "10:00"
    - "13:00"
    - "16:00"
    - "19:00"
    - "21:00"

content:
  source: "csv"          # "csv" または "json"
  csv_path: "posts/posts.csv"
  json_path: "posts/posts.json"

duplicate_check:
  similarity_threshold: 0.85   # 0.0〜1.0（高いほど厳しい）
```

---

## CSV/JSONの書き方

### posts.csv

```csv
id,content,category,created_at
1,"投稿本文をここに書く",カテゴリ,2024-01-01
```

- `content` に改行を含める場合は `"..."` で囲む
- 改行は `\n` ではなく実際の改行でOK（ダブルクォートで囲む）

### posts.json

```json
[
  {
    "id": "1",
    "content": "投稿本文\n\n複数行もOK",
    "category": "カテゴリ",
    "created_at": "2024-01-01"
  }
]
```

---

## 実行方法

### テスト実行（dry-run）

APIへは送信せず、ログだけ確認できます。

```powershell
python scripts/schedule_posts.py --dry-run
```

または

```powershell
python main.py --dry-run
```

### 本番実行

Typefully APIへ予約投稿を送信します。

```powershell
python scripts/schedule_posts.py --execute
```

または

```powershell
python main.py --execute
```

---

## Windowsでの毎日自動実行設定（タスクスケジューラー）

毎朝7:00に自動実行するタスクを登録します。

### PowerShellで一発設定

```powershell
$action = New-ScheduledTaskAction `
  -Execute "python" `
  -Argument "C:\Users\shota\threads-os\main.py --execute" `
  -WorkingDirectory "C:\Users\shota\threads-os"

$trigger = New-ScheduledTaskTrigger -Daily -At "07:00"

$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 5)

Register-ScheduledTask `
  -TaskName "ThreadsAutoPost" `
  -Action $action `
  -Trigger $trigger `
  -Settings $settings `
  -RunLevel Highest `
  -Force
```

### 確認・削除

```powershell
# 登録確認
Get-ScheduledTask -TaskName "ThreadsAutoPost"

# 削除
Unregister-ScheduledTask -TaskName "ThreadsAutoPost" -Confirm:$false
```

---

## 重複チェックの仕組み

- `logs/posted_log.csv` に過去の予約済み投稿を保存
- 新規投稿のMD5ハッシュで完全一致チェック
- `difflib.SequenceMatcher` で類似度チェック（閾値は `config.yaml` で設定）
- 重複と判定された投稿はスキップされ、ログに記録される

---

## 拡張予定（今後追加可能な機能）

- `--ai-generate` オプションでClaude/GPTが投稿文を自動生成
- 競合アカウントのバズ投稿を参考にした自動リサーチ
- Slack / LINE通知（予約完了をリアルタイム通知）
- Typefully上の予約スロットと照合して二重予約を防ぐ
