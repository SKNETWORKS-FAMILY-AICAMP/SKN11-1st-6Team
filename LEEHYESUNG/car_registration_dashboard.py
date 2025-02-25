import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# MySQL 연결
def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="mysql_user1",
        password="mysql_user1",
        database="car_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car_registration")
    result = cursor.fetchall()
    conn.close()
    return pd.DataFrame(result, columns=["id", "year", "car_type", "registration_count"])

# Streamlit 앱
st.title("🚗 중고차 등록 추이 분석")

# 데이터 불러오기
df = get_data()

# 연도별 등록 추이 시각화
fig = px.line(df, x="year", y="registration_count", color="car_type", title="연도별 자동차 등록 추이")
st.plotly_chart(fig)

# 데이터 테이블 표시
st.dataframe(df)

# 특정 연도 선택 필터
year_filter = st.selectbox("조회할 연도를 선택하세요", df["year"].unique())
filtered_df = df[df["year"] == year_filter]
st.write(f"선택한 연도({year_filter})의 데이터")
st.dataframe(filtered_df)
