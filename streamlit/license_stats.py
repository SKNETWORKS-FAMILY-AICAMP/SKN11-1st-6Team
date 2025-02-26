import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# MySQL 연결 정보
username = 'root'
password = '030617'
host = 'localhost'
port = '3306'
database = 'not_temu_project'

# SQLAlchemy 연결 문자열
connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# 🔍 도시 검색 기능
st.title("🚗 도시별 운전면허 및 차량 밀도 통계")

# 🔄 세션 상태 초기화
if "search_city" not in st.session_state:
    st.session_state.search_city = ""

if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = False  # 리셋 트리거 상태

# 🔄 리셋 버튼 클릭 시 검색어 초기화
def reset_search():
    st.session_state.search_city = ""  # 검색어 초기화
    st.session_state.reset_trigger = True  # 트리거 활성화

# 🔄 리셋 트리거 감지 → 페이지 리셋
if st.session_state.reset_trigger:
    st.session_state.reset_trigger = False  # 트리거 리셋
    st.rerun()  # 전체 페이지 새로고침

# 검색 입력창 (세션 상태와 동기화)
search_city = st.text_input("검색할 도시 이름을 입력하세요 (예: 서울특별시)", value=st.session_state.search_city).strip()

# 검색어를 입력할 때마다 세션 상태 업데이트
st.session_state.search_city = search_city

# 검색 쿼리
search_query = """
SELECT 
    c.city_name AS '도시',
    c.density AS '인구 밀도',
    c.car_amount AS '차량 등록수' ,
    c.license_population AS '운전면허 보유수',
    c.population AS '인구 수',
    v.vehicle_name AS '추천',
    (c.car_amount / NULLIF(c.density, 0)) AS '밀도 대비 차량 등록 수치'
FROM license l
LEFT JOIN city c ON l.is_license = c.license
LEFT JOIN vehicle v ON v.need_license = l.is_license
WHERE c.city_name LIKE %s
ORDER BY (c.car_amount / NULLIF(c.density, 0)) ASC;
"""

# 전체 데이터 조회 쿼리
full_query = """
SELECT 
    c.city_name AS '도시',
    c.density AS '인구밀도',
    c.car_amount AS '차량 등록 수',
    c.license_population AS '운전면허 보유 수',
    c.population AS '인구 수',
    CASE 
        WHEN c.license = 1 THEN '렌트카, 전동 킥보드'
        WHEN c.license = 0 THEN '자전거, 택시'
        ELSE '알 수 없음'
    END AS '추천',
    (c.car_amount / NULLIF(c.density, 0)) AS '밀도 대비 차량 등록 수치'
FROM license l
LEFT JOIN city c ON l.is_license = c.license
ORDER BY (c.car_amount / NULLIF(c.density, 0)) ASC;
"""

# 검색 결과 또는 전체 데이터 표시 로직
if search_city:
    try:
        search_df = pd.read_sql(search_query, engine, params=(f"%{search_city}%",))
        st.session_state.search_city = ""
        
        if search_df.empty:
            st.warning("해당 도시의 데이터가 없습니다.")
        else:
            # 검색 결과 제목과 리셋 버튼을 한 줄에 배치
            col1, col2 = st.columns([5, 1])
            with col1:
                st.subheader(f"📍 '{search_city}' 검색 결과")
            with col2:
                st.button("🔄 리셋", on_click=reset_search)  # 검색 리셋 버튼
            
            st.dataframe(search_df)
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류 발생: {e}")
else:
    try:
        # 전체 데이터 제목과 리셋 버튼을 한 줄에 배치
        col1, col2 = st.columns([5, 1])
        with col1:
            st.subheader("📊 전체 도시 데이터")
        with col2:
            st.button("🔄 리셋", on_click=reset_search)  # 전체 데이터 리셋 버튼
        
        full_df = pd.read_sql(full_query, engine)
        st.dataframe(full_df)  # 검색 전 전체 데이터 표시
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류 발생: {e}")
