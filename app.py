import streamlit as st
import time
from weather import get_weather
from PIL import Image


st.title("Weather Wear AI")

input_num = st.number_input('Input a number', value=110010)

if st. button ("BUTTON"):
    with st.spinner('気象情報を取得しています...'):
        result_weather = get_weather(input_num)
        time.sleep(2)
        st.write("気象情報：\n", result_weather)

