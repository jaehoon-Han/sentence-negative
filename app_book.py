import pandas as pd
import streamlit as st
import random


best_book = pd.read_csv('data/best_book_2021_12.csv')
best_book.dropna(axis=0, subset = ['description','img_url'],inplace = True)
best_book = best_book.loc[:,['title','author','description','img_url','age']]
best_book_not = best_book.loc[:,['title','author','description','age']]
df_index1 = best_book.loc[best_book['age'].str.contains('청소년')== True, ].index
df_index2 = best_book.loc[best_book['age'].str.contains('영유아')== True, ].index
df_index3 = best_book.loc[best_book['age'].str.contains('유아')== True, ].index
df_index4 = best_book.loc[best_book['age'].str.contains('초등')== True, ].index

best_book.drop(df_index1, inplace= True)
best_book.drop(df_index2, inplace= True)
best_book.drop(df_index3, inplace= True)
best_book.drop(df_index4, inplace= True)
best_book = best_book['age'].dropna()

best_book.drop_duplicates('title')


def run_book() :

    
    st.image(best_book.loc[random.randint(0,2136), 'img_url'])
    st.image(best_book.loc[random.randint(2167,4272), 'img_url'])
    st.image(best_book.loc[random.randint(4273,6418), 'img_url'])
    st.dataframe(best_book_not)

