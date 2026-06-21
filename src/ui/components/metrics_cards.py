import streamlit as st


def metric(label: str, value):
    st.metric(label, value)
