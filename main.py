import streamlit as st

from gigachat_api import (
    get_access_token,
    sent_prompt_and_get_response,
)

st.title("Чат бот")


def add_message(role: str, message: str, is_image: bool = False):
    if is_image:
        st.chat_message(role).image(message)
    else:
        st.chat_message(role).write(message)
    st.session_state.messages.append(
        {"role": role, "content": message, "is_image": is_image}
    )


if "access_token" not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
    except:
        st.toast("Не удалось получить токен")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "С чем вам помочь?", "is_image": False}
    ]

for msg in st.session_state.messages:
    if msg["is_image"]:
        st.chat_message(msg["role"]).image(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

if user_prompt := st.chat_input():
    add_message("user", user_prompt)
    with st.spinner("В процессе..."):
        response, is_image = sent_prompt_and_get_response(
            user_prompt, st.session_state.access_token
        )
    add_message("ai", response, is_image)
