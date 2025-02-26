import streamlit as st
from streamlit_app import chart_df
import plotly.express as px


chart_df['density_ratio'] = chart_df['density'] / chart_df['car_amount']


title="전국 인구 밀도 대비 자동차 등록 현황"
st.title(title)
fig = px.pie(chart_df, names='city_name', values='density_ratio')

fig.update_layout(
    width=600,  
    height=600,  
)

st.plotly_chart(fig)
