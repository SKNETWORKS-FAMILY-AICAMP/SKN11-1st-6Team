import pandas as pd
import mysql.connector
from fractions import Fraction
import statistics

# MySQL 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="mysql_user1",
    password="mysql_user1",
    database="car_db"
)
cursor = conn.cursor()

# 첫 번째 CSV 파일 (car_amount)
df_car_amount = pd.read_csv('/Users/comet39/SKN_bootcamp/first_project/SKN011-1st-6Team/LEEHYESUNG/201001_total.csv')

# 두 번째 CSV 파일 (license)
df_license = pd.read_csv('/Users/comet39/SKN_bootcamp/first_project/SKN011-1st-6Team/license.csv', encoding='UTF-8')

# 두 번째 CSV 파일 (population)
df_population = pd.read_csv('/Users/comet39/SKN_bootcamp/first_project/SKN011-1st-6Team/population_densityl.csv')

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
    car_amount = int(row['Total'].replace(',', ''))
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
