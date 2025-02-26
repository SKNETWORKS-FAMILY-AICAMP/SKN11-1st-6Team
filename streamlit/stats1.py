import streamlit as st
import plotly.express as px
import geopandas as gpd
import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from streamlit_app import chart_df


geojson_path = "korea_map_simplified.geojson"
with open(geojson_path, encoding="utf-8") as f:
    korea_geojson = json.load(f)

fig = px.choropleth_mapbox(
    chart_df,
    geojson=korea_geojson,
    locations="city_name",  
    featureidkey="properties.CTP_KOR_NM", 
    color="density",
    color_continuous_scale="Blues",
    mapbox_style="carto-positron",
    center={"lat": 36, "lon": 127.5},
    zoom=6,
    hover_data=["city_name", "density", "car_amount"]
)

fig.update_layout(
    width=700,
    height=800,
    hoverlabel=dict(  # 🔹 마우스 오버 시 글씨 크기 조정
        font=dict(size=20, color="white"),  # 글씨 크기와 색상
        bgcolor="black",  # 배경색 설정
    )
)

fig.update_traces(
    hovertemplate=
    '<b>%{customdata[0]}</b><br>'
    '<b>차량등록수: %{customdata[2]}</b><br>' 
    '인구밀도: %{z}<br>'
    
)

st.title("전국 자동차 등록 현황")
st.plotly_chart(fig)