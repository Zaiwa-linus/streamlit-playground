import streamlit as st
import pandas as pd
import numpy as np

# ページの設定
st.set_page_config(page_title="Simple Streamlit App", layout="wide")

# タイトル
st.title("Welcome to the Simple Streamlit App")

# テキスト入力
name = st.text_input("What's your name?", "Guest")
st.write(f"Hello, {name}! This is a demonstration of Streamlit's capabilities.")

# スライダーで数値入力
value = st.slider("Choose a value for our dataset", 10, 100, 50)
st.write(f"You selected: {value}")

# ランダムデータの生成
data = pd.DataFrame(
    np.random.randn(value, 3),
    columns=["Feature A", "Feature B", "Feature C"]
)

# データフレームの表示
st.write("Here is a preview of the dataset:")
st.dataframe(data)

# グラフの表示
st.write("Line Chart of the Random Data:")
st.line_chart(data)

st.write("Bar Chart of the Random Data:")
st.bar_chart(data)

# セレクトボックス
chart_type = st.selectbox(
    "Choose a chart type to display:",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

# 条件に応じたチャート表示
st.write(f"You selected: {chart_type}")
if chart_type == "Line Chart":
    st.line_chart(data)
elif chart_type == "Bar Chart":
    st.bar_chart(data)
else:
    st.area_chart(data)

# フッター
st.write("Thank you for trying this app!")