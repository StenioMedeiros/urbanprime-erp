import streamlit as st


def text_input(label: str, key: str):
    return st.text_input(label, key=key)
