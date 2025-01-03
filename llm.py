from google import genai
from google.genai import types
import vertexai
from vertexai.generative_models import GenerativeModel, Image
import settings

PROJECT_ID = settings.PROJECT_ID
LOCATION = settings.LOCATION
IMAGEN_MODEL = settings.IMAGEN_MODEL
GEMINI_MODEL = settings.GEMINI_MODEL

def generate(conditions: str) -> str:
  """
  指定された天気条件に基づいて服装の提案を生成します。

  Args:
    conditions (str): 天気条件を表す文字列。

  Returns:
    str: 生成された服装の提案。
  """
  client = genai.Client(
      vertexai=True,
      project=PROJECT_ID,
      location=LOCATION
  )

  text1 = types.Part.from_text(f"""{conditions}
上記の条件にあう服装を考えてください。
回答は以下の形式で必要な内容だけ回答してください。
トップス：
ボトムス：
アウター：
足元：
小物：""")

  contents = [
    types.Content(
      role="user",
      parts=[
        text1
      ]
    )
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 0,
    top_p = 0.95,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text("""あなたはプロフェッショナルの服装コーディネーターです。""")],
  )

  result = client.models.generate_content(
    model = GEMINI_MODEL,
    contents = contents,
    config = generate_content_config,
  )
  print(result)
  return result.text


def generate_description(image_path: str) -> str:
  """
  指定された画像パスから画像を読み込み、コーディネートの解説を生成する。

  Args:
    image_path (str): 画像ファイルのパス。

  Returns:
    str: 生成されたコーディネートの解説テキスト。
  """
  vertexai.init(project=PROJECT_ID, location=LOCATION)
  model = GenerativeModel(GEMINI_MODEL)

  contents = [
    Image.load_from_file(image_path),
    """添付画像のコーディネートを以下の内容で解説してください。前置きは不要で以下の内容だけ返してください。

全体的な印象：
各アイテムの詳細：
コーディネートのポイント：
その他：
おすすめのシーン："""]

  # Query the model
  response = model.generate_content(contents=contents)
  # print(response.text)
  return response.text


if __name__ == '__main__':
    pass