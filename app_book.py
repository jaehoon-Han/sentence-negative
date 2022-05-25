import pandas as pd
import streamlit as st
import random


best_book = pd.read_csv('data/best_book_2021_12.csv')
best_book = best_book.loc[:,['title','author','description','img_url','rank']]

def run_book() :

    
    st.image(best_book.loc[random.randint(0,97988), 'img_url'])
    st.image(best_book.loc[random.randint(0,97988), 'img_url'])
    st.image(best_book.loc[random.randint(0,97988), 'img_url'])
    


