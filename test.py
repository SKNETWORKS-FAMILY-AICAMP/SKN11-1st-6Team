import pandas as pd
from sqlalchemy import create_engine
import json

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

car_reg_df = pd.read_csv('car_reg_202501.csv')
car_reg_df.rename(columns={'시도명': '지역'}, inplace=True)
car_reg_df['지역'] = car_reg_df['지역'].map(region_map)

merged_df = pd.merge( df_clean, car_reg_df, left_on='지역', right_on='지역', how='left')



merged_df = merged_df.rename(columns={
    "지역": "city_name",
    "인구": "population",
    "인구밀도": "density",
    "차량합계": "car_amount"
})

# engine = create_engine('mysql+pymysql://username:password@localhost/mydatabase')    # db에 따라 수정 요망
engine = create_engine('mysql+pymysql://root:1092@localhost/mydb')

merged_df.to_sql('population_data', con=engine, if_exists='replace', index=False)

# 결과 출력
print(merged_df)
