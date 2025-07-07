import streamlit as st
import random

st.set_page_config(page_title="Guess the Number", page_icon="🎲", layout="centered")

# ---------- 1. 初始化 Session State ----------
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.min_value = 1
    st.session_state.max_value = 100
    st.session_state.message = "遊戲開始！請猜一個數字。"

# ---------- 2. 版面 ----------
st.title("🎲 猜數字遊戲")
st.write("我心裡想了一個 **1 ~ 100** 的整數，你能在最少次數內猜中嗎？")

st.info(f"請輸入 **{st.session_state.min_value} ~ {st.session_state.max_value}** 之間的數字")

guess = st.number_input(
    label="你的猜測",
    min_value=st.session_state.min_value,
    max_value=st.session_state.max_value,
    step=1,
    key="guess_input",
)

col1, col2 = st.columns([1, 1])
with col1:
    guess_btn = st.button("猜！", use_container_width=True)
with col2:
    reset_btn = st.button("重新開始", use_container_width=True)

# ---------- 3. 遊戲邏輯 ----------
if guess_btn:
    g = int(guess)
    min_v, max_v, secret = (
        st.session_state.min_value,
        st.session_state.max_value,
        st.session_state.secret,
    )

    if g < min_v or g > max_v:
        st.session_state.message = f"⚠️ 請輸入 {min_v} ~ {max_v} 之間的數字！"
    elif g == secret:
        st.balloons()
        st.session_state.message = f"🎉 恭喜！答案正是 **{secret}**"
    elif g < secret:
        st.session_state.message = "太小了，再試一次！"
        st.session_state.min_value = g
        st.rerun()
    else:  # g > secret
        st.session_state.message = "太大了，再試一次！"
        st.session_state.max_value = g
        st.rerun()

# ---------- 4. 重新開始 ----------
if reset_btn or st.session_state.min_value > st.session_state.max_value:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.min_value = 1
    st.session_state.max_value = 100
    st.session_state.message = "已重設！請重新猜一個數字。"
    st.rerun()

# ---------- 5. 當前狀態提示 ----------
st.success(st.session_state.message)
