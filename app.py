import streamlit as st
import time
from weather import get_weather
from llm import generate_coordination
# from imagen import generate_image
from PIL import Image

st.title("Weather Wear AI")

input_num = st.number_input('Input a number', value=110010)

if st. button ("BUTTON"):
    with st.spinner('気象情報を取得しています...'):
        result_weather = get_weather(input_num)
        time.sleep(2)
        st.write("気象情報：\n", result_weather)
    with st.spinner('コーディネートを作成中しています...'):
        cordinate_prompt = generate_coordination(conditions=result_weather)
        time.sleep (2)
        st.write('プロンプト：', cordinate_prompt)
    # with st.spinner('イメージ画像を生成しています...'):
    #     result_image = generate_image(prompt=cordinate_prompt + "n色合いは暖色系で統一してください")
    #     time.sleep (2)
    #     st.write('result_image: ', result_image)
    #     img = Image.open ("input-image.png")
    #     st.image(img)
