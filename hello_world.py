"""
Hello World App - シンプルなStreamlitアプリの例
"""

import streamlit as st

# Page configuration
st.set_page_config(page_title="Hello World", page_icon="👋", layout="centered")

# Main content
st.title("👋 Hello World")
st.write("**Streamlitへようこそ！**")

# Simple interaction
name = st.text_input("あなたの名前を入力してください:")

if name:
    st.success(f"こんにちは、{name}さん！")
    st.balloons()

# Information
st.info("これはStreamlitテンプレートのサンプルアプリです。")
