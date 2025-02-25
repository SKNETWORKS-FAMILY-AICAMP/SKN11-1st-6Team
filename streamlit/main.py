import streamlit as st
from streamlit_app import chart_df

st.title("Statistics Page")
st.write("DB에서 가져온 데이터:")
st.dataframe(chart_df)
