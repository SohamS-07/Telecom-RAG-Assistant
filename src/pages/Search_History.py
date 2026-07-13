import streamlit as st
import pandas as pd
import os

st.title("Search History")
if os.path.exists("search_history.csv"):
    df=pd.read_csv("search_history.csv")
    st.dataframe(df,use_container_width=True)
else:
    st.info("No Searches made yet")