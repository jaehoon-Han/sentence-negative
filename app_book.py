import pandas as pd
import streamlit as st


def run_book() :
    st.dataframe(pd.read_csv('data/best_book_2021_12.csv'))
    st.image('http://image.aladin.co.kr/product/5100/19/cover/8925554992_1.jpg')
    st.text()