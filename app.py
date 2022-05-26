import pandas as pd
import numpy as np
import streamlit as st

from app_book import run_book



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