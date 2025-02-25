import streamlit as st
import plotly.express as px
import geopandas as gpd
import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine

xls = pd.ExcelFile('population_density.xlsx', engine="openpyxl")

df_clean = pd.read_excel(xls, sheet_name="Sheet0", skiprows=3)

df_clean.columns = ["지역", "인구", "인구밀도"]

df_clean = df_clean.dropna()

df_clean["인구"] = df_clean["인구"].astype(str).str.replace(",", "").astype(int)
df_clean["인구밀도"] = df_clean["인구밀도"].astype(str).str.replace(",", "").astype(int)
df_clean = df_clean[df_clean['지역'] != '수도권']
df_clean = df_clean[df_clean['지역'] != '계']
df_clean = df_clean.reset_index(drop=True)

region_map = {
    '서울': '서울특별시',
    '부산': '부산광역시',
    '대구': '대구광역시',
    '인천': '인천광역시',
    '광주': '광주광역시',
    '대전': '대전광역시',
    '울산': '울산광역시',
    '세종': '세종특별자치시',
    '경기': '경기도',
    '강원': '강원특별자치도',
    '충북': '충청북도',
    '충남': '충청남도',
    '전북': '전라북도',
    '전남': '전라남도',
    '경북': '경상북도',
    '경남': '경상남도',
    '제주': '제주특별자치도'
}

df_clean['지역'] = df_clean['지역'].replace(region_map)

df_density = df_clean.drop(columns=['인구'])

# engine = create_engine('mysql+pymysql://username:password@localhost/mydatabase')    # db에 따라 수정 요망
engine = create_engine('mysql+pymysql://root:1092@localhost/mydb')

df_clean.to_sql('population_data', con=engine, if_exists='replace', index=False)

print(df_density)

geojson_path = "korea_map_simplified.geojson"
with open(geojson_path, encoding="utf-8") as f:
    korea_geojson = json.load(f)

fig = px.choropleth_mapbox(
    df_density,
    geojson=korea_geojson,
    locations="지역",  
    featureidkey="properties.CTP_KOR_NM", 
    color="인구밀도",
    color_continuous_scale="Blues",
    mapbox_style="carto-positron",
    center={"lat": 36.5, "lon": 127.5},
    zoom=6,
    hover_data=["지역", "인구밀도"]
)

fig.update_layout(
    width=700,
    height=1000
)


st.title("대한민국 지도 데이터 시각화")
st.plotly_chart(fig)