import pandas as pd
import numpy as np
import streamlit as st

best_book = pd.read_csv('data/best_book_2021_12.csv')
best_book =best_book.loc[:,['title','author','description','img_url','rank']]
