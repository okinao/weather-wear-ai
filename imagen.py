import settings
import os
import google.generativeai as genai

# キー情報など固定値を定数定義
GEMINI_API_KEY = settings.GEMINI_API_KEY
IMAGEN_MODEL = settings.IMAGEN_MODEL


def generate_image():
    genai.configure(api_key=GEMINI_API_KEY)

    imagen = genai.ImageGenerationModel(IMAGEN_MODEL)

    result = imagen.generate_images(
        prompt="Fuzzy bunnies in my kitchen",
        number_of_images=4,
        safety_filter_level="block_only_high",
        person_generation="allow_adult",
        aspect_ratio="3:4",
        negative_prompt="Outside",
    )

    for image in result.images:
        print(image)

    # Open and display the image using your local operating system.
    for image in result.images:
        image._pil_image.show()
    
    return

if __name__ == "__main__":
    # デバッグ用
    conditions1 = "トップス：長袖シャツ、薄手ニット ボトムス：ロングパンツ（デニム、チノパンなど） アウター：ミドル丈のコート（ウール、ダウンなど） 足元：スニーカー、ブーツ 小物：マフラー、手袋（気温に応じて）"
    conditions2 = "2025年01月04日の埼玉県 さいたま の天気は晴時々曇です。 最高気温は9度、最低気温は0度です。 降水確率は0時から6時まで10%、6時から12時まで0%、12時から18時まで0%、18時から24時まで10%です"
    prompt = conditions1 + "\n上記を参考にしながら以下の気象条件にあうコーディネートのイメージ画像を生成してください。\n" + conditions2
    # result = generate_image(prompt)
    result = generate_image()
    # print(result)