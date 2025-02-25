import streamlit as st
import plotly.express as px
import geopandas as gpd
import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine


username = 'root'  
password = '1092' 
host = 'localhost'  
port = '3306' 
database = 'mydb' 

connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string)

table_name = 'population_data'  
query = f"SELECT * FROM {table_name}"

chart_df = pd.read_sql(query, engine)

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
    center={"lat": 36.5, "lon": 127.5},
    zoom=6,
    hover_data=["city_name", "density", "car_amount"]
)

fig.update_layout(
    width=700,
    height=1000
)

fig.update_traces(
    hovertemplate=
    '<b>%{customdata[0]}</b><br>'
    '인구밀도: %{z}<br>'
    '차량등록수: %{customdata[2]}<br>' 
)

st.title("Chart Title")
st.plotly_chart(fig)
