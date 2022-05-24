import pandas as pd
import numpy as np
import streamlit as st

from app_book import run_book

df1 = pd.read_csv('data/NL_bo_sense_2019.csv')
df2 = pd.read_csv('data/NL_BO_SENSE_2021.csv')
df3 = pd.read_csv('data/NL_BO_SENSE_202012.csv')



def main() :
    st.title('책 추천 앱')
    menu = ['Home','BOOK','Recommend']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        pass
    elif choice==menu[1] :
        run_book()
    else :
        pass

        


if __name__ == '__main__' :
    main()