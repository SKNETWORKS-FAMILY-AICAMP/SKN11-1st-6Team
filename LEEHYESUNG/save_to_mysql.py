import mysql.connector
import pandas as pd

# MySQL 연결
conn = mysql.connector.connect(
    host="localhost",
    user="mysql_user1",
    password="mysql_user1",
    database="car_db"
)
cursor = conn.cursor()

# 데이터 삽입 함수
def insert_data(df):
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO city_test (city, total) 
            VALUES (%s, %s)
        """, (row["City"], row["Toal"]))
    conn.commit()

# 데이터 불러오기 함수
# def get_data():
#     cursor.execute("SELECT * FROM CITY")
#     result = cursor.fetchall()
#     return pd.DataFrame(result, columns=["id", "year", "car_type", "registration_count"])

# CSV 파일 읽어서 DB에 저장
df = pd.read_csv("/Users/comet39/SKN_bootcamp/first_project/201001_total.csv")
data_list = df.values.tolist()
print(data_list)  # [[row1_col1, row1_col2, ...], [row2_col1, row2_col2, ...], ...]

insert_data(df)

# 데이터 조회 확인
# print(get_data())

# 연결 종료
cursor.close()
conn.close()
