from google import genai
import settings

# キー情報など固定値を定数定義
GEMINI_API_KEY = settings.GEMINI_API_KEY
GEMINI_MODEL = settings.GEMINI_MODEL


def generate_coordination(conditions):
    client = genai.Client(api_key=GEMINI_API_KEY)

    contents = f"""{conditions}
上記の条件にあう服装を考えてください。
回答は以下の形式で必要内容だけ回答してください。
トップス：
ボトムス：
アウター：
足元：
小物："""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=contents
    )
    return response.text

if __name__ == "__main__":
    # デバッグ用
    conditions = "2025年01月04日の埼玉県 さいたま の天気は晴時々曇です。 最高気温は9度、最低気温は0度です。 降水確率は0時から6時まで10%、6時から12時まで0%、12時から18時まで0%、18時から24時まで10%です"
    result = generate_coordination(conditions)
    print(result)