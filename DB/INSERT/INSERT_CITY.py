import pandas as pd
import mysql.connector
from fractions import Fraction
import statistics

# MySQL 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="030617",
    database="not_temu_project"
)
cursor = conn.cursor()

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

# 첫 번째 CSV 파일 (car_amount)
df_car_amount = pd.read_csv('데이터/car_reg_202501.csv')
df_car_amount['시도명'] = df_car_amount['시도명'].replace(region_map)
df_car_amount.rename(columns={'차량합계': 'Total'}, inplace=True)
df_car_amount.rename(columns={'시도명': 'City'}, inplace=True)

# 두 번째 CSV 파일 (license)
df_license = pd.read_csv('데이터/license.csv', encoding='UTF-8')
df_license['City'] = df_license['City'].replace(region_map)

# 두 번째 CSV 파일 (population)
df_population = pd.read_csv('데이터/population_densityl.csv')
df_population['City'] = df_population['City'].replace(region_map)

# 두 CSV 파일을 'city_name'을 기준으로 병합
df_temp = pd.merge(df_car_amount, df_license, on='City', how='outer')
df = pd.merge(df_temp, df_population, on='City', how='outer')

list = []
for index,row in df.iterrows():
    list.append(int(row['Popular'].replace(',', ''))*1000-int(row['1종보통'].replace(',', ''))+int(row['2종보통'].replace(',', '')))
    
median_value = statistics.median(list)

# 중복된 city_name을 기준으로 합치기 (car_amount, license_population 컬럼 업데이트)
for index, row in df.iterrows():
    city_name = row['City']
    car_amount = int(row['Total'])
    license_population = int(row['1종보통'].replace(',', ''))+int(row['2종보통'].replace(',', ''))
    density=int(row['Density'].replace(',', ''))
    popular=int(row['Popular'].replace(',', ''))
    
    if median_value>(int(row['Popular'].replace(',', ''))*1000-int(row['1종보통'].replace(',', ''))+int(row['2종보통'].replace(',', ''))): 
        license=True
    else : license=False
    
    # 이미 존재하는 city_name을 업데이트
    cursor.execute("""
        INSERT INTO city (city_name, car_amount, license_population, population, density,license)
        VALUES (%s, %s, %s, %s, %s,%s)
        ON DUPLICATE KEY UPDATE
            car_amount = VALUES(car_amount),
            license_population = VALUES(license_population)
    """, (city_name, car_amount,license_population,popular*1000,density,license))

# 커밋 후 연결 종료
conn.commit()
cursor.close()
conn.close()
