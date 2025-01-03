import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import settings

PROJECT_ID = settings.PROJECT_ID
LOCATION = settings.LOCATION
IMAGEN_MODEL = settings.IMAGEN_MODEL

vertexai.init(project=PROJECT_ID, location=LOCATION)

def generate_image(prompt: str) -> None:
    """
    指定されたプロンプトに基づいて画像を生成し、保存する関数。

    Args:
        prompt (str): 画像生成のためのテキストプロンプト。

    Returns:
        None: この関数は何も返しませんが、生成された画像をファイルに保存します。
    """
    model = ImageGenerationModel.from_pretrained(IMAGEN_MODEL)

    images = model.generate_images(
        prompt=prompt,
        number_of_images=2,
        language="ja",
        aspect_ratio="1:1",
        safety_filter_level="block_some",
        person_generation="allow_adult",
    )

    for i, image in enumerate(images, 1):
        output_file = f"images/image-{i}.png"
        image.save(location=output_file, include_generation_parameters=False)
        print(f"ファイル名: {output_file}, サイズ: {len(image._image_bytes)} bytes")

    return

if __name__ == '__main__':
    pass