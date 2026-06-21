import streamlit as st


def require_login() -> None:
    if "access_token" not in st.session_state:
        st.stop()
