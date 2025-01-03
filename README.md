# weather-wear-ai
The App that teach you what to wear tomorrow.

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

# 生成AIの利用に関する説明
## 使用するモデル
自由会話：`gemini-2.0-flash-exp`
画像生成：
参考：(試験運用版モデル)[https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=ja]

## SDKの使用
参考：(Google Gen AI SDK)[https://ai.google.dev/gemini-api/docs/sdks?hl=ja]
### imagen用のPythonパッケージ
Python SDKの安定版にはImagenがサポートされていない為、PyPlからではなくimagenのGitHubブランチからダンロードする
```shell
pip install -U git+https://github.com/google-gemini/generative-ai-python@imagen
```