import streamlit as st
from streamlit_app import faq
import plotly.express as px

st.markdown("""
    <style>
        div[data-baseweb="tab-list"] button {
            margin-right: 15px !important;  /* 탭 간격 조정 */
            padding: 10px 20px !important; /* 탭 내부 여백 */
            font-size: 30px !important;  /* 글자 크기 */
        }
        
        # div[class="st-emotion-cache-b95f0i e6rk8up4"]{
        #     color: black;
        #     }
    </style>
""", unsafe_allow_html=True)


dart, g_coo, blue, nemo = st.tabs(["🛴Dart", '🛴GCOO🚴🏻‍♂️', '🚕카카오T BLUE', '🚕네모택시'])
with dart:
    for i in range(9):
        with st.expander(f"**{faq['question'][i].replace(":", ".")}**"):
            st.write(faq["answer"][i])
with g_coo:
    for j in range(9, 22):
        with st.expander(f"**Q. {faq['question'][j]}**"):
            st.write(faq["answer"][j])

with blue:
    for k in range(22, 29):
        with st.expander(f"**Q. {faq['question'][k]}**"):
            st.write(faq["answer"][k])

with nemo:
    for t in range(29, 42):
        with st.expander(f"**Q. {faq['question'][t]}**"):
            st.write(faq["answer"][t])