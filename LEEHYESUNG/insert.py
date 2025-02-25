import pandas as pd
from sqlalchemy import create_engine

# MySQL 연결 정보 설정
MYSQL_HOST = "localhost"
MYSQL_USER = "mysql_user1"
MYSQL_PASSWORD = "mysql_user1"
MYSQL_DB = "car_db"
MYSQL_TABLE = "city"

# SQLAlchemy 엔진 생성
engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}")

# 엑셀 파일 로드
file_path = "/Users/comet39/SKN_bootcamp/first_project/자동차등록현황보고 전체 일단 다합친거.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

selected_columns = ['월(Monthly)', '시도', '시군구']  # 원하는 컬럼명으로 변경
df_selected = df[selected_columns]

# MySQL에 삽입
df_selected.to_sql(name=MYSQL_TABLE, con=engine, if_exists="append", index=False)


# 데이터 삽입 (if_exists="replace" → 기존 테이블 덮어쓰기, "append" → 기존 데이터 유지)
df.to_sql(name=MYSQL_TABLE, con=engine, if_exists="append", index=False)
