# 服装コーディネートAI
このアプリでは明日の気象情報に合わせて服装のコーディネート案を画像で提示してくれます。

## 仮想環境
```shell
python -m venv .venv
source .venv/bin/activate
```

## ライブラリのインストール
```shell
pip install -r requirements.txt
```

## 実行方法
```shell
streamlit run app.py
```

## 生成AIの利用に関する説明

### 使用するモデル

自由会話：`gemini-2.0-flash-exp`

画像生成：`imagen-3.0-generate-001`
