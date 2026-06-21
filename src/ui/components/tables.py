import streamlit as st


def table(rows):
    st.dataframe(rows, use_container_width=True)
