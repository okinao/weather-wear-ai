import streamlit as st
import time
from weather import get_weather
from llm import generate, generate_description
from imagen import generate_image
from PIL import Image


st.title("服装コーディネートAI")

select_sex = st.selectbox(
    "性別を選択してください",
    ["男性", "女性", ""],
    placeholder="性別を選択してください"
)

select_age = st.selectbox(
    "年齢を選択してください",
    ["10代", "20代", "30代", "40代", "50代", "60代以上"],
    placeholder="年齢を選択してください"
)

select_city = st.selectbox(
    "地域を選択してください",
    ["北海道/札幌: 016010",
    "新潟県/新潟: 150010",
    "東京都/東京: 130010",
    "愛知県/名古屋: 230010",
    "大阪府/大阪: 270000",
    "岡山県/岡山: 330010",
    "広島県/広島: 340010",
    "高知県/高知: 390010",
    "福岡県/福岡: 400010",
    "鹿児島県/鹿児島: 460010",
    "沖縄県/那覇: 471010",
    ],
    index=2,
    placeholder="都市を選択してください"
)

city_name, city_id = select_city.split(": ")

if st.button("BUTTON"):
    with st.spinner('気象情報を取得しています...'):
        result_weather = get_weather(city_id)
        time.sleep(2)
        st.subheader(f"{city_name}の気象情報")
        st.write(result_weather)

    with st.spinner('コーディネート案を作成中しています...'):
        coordinate_prompt = generate(conditions=result_weather)
        time.sleep(2)
        st.subheader("コーディネート案")
        st.write(coordinate_prompt)

    with st.spinner('コーディネート画像を生成しています...'):
        generate_image(prompt=f"{coordinate_prompt}\n上記を参考にしながら以下の気象条件にあうコーディネートのイメージ画像を生成してください。なお、性別は{select_sex}、年齢は{select_age}です。\n{result_weather}")
        time.sleep(2)
        
        num = 2
        col = st.columns(num)

        for i in list(range(0, num, 1)):
            # with col[i]:
            image_path = f"images/image-{i+1}.png"
            st.subheader(f"コーディネート{i+1}")
            st.image(image_path, use_container_width=True)
            with st.expander("AI解説", expanded=False):
                description = generate_description(image_path)
                st.write(description)

    st.success('コーディネート例を生成しました。')