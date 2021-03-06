import pandas as pd
import streamlit as st
import random
import seaborn as sns


def run_book() :
    best_book = pd.read_csv('data/best_book_2021_12.csv')
    best_book.dropna(axis=0, subset = ['description','img_url'],inplace = True)
    best_book = best_book.loc[:,['title','author','description','img_url','age']]
    best_book['age'] = best_book['age'].dropna()

    
    best_book20 = best_book[best_book['age'].str.contains('20대')==True]
    best_book30 = best_book[best_book['age'].str.contains('30대')==True]
    best_book2030 = pd.concat([best_book20,best_book30]).reset_index()
    best_book2030_not = best_book2030.loc[:,['title','author','description','age']]


    st.image(best_book2030.loc[random.randint(0,best_book2030.shape[0]), 'img_url'])
    st.image(best_book2030.loc[random.randint(0,best_book2030.shape[0]), 'img_url'])
    st.image(best_book2030.loc[random.randint(0,best_book2030.shape[0]), 'img_url'])
         
    st.dataframe(best_book2030_not)
    best_book.rename