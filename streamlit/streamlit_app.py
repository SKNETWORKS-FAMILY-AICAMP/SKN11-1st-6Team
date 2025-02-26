import streamlit as st
from sqlalchemy import create_engine
import pandas as pd


host="localhost"
user="root"
password="030617"
database="not_temu_project"    # 해당 부분 db에 맞게 변경

connection_string = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"

engine = create_engine(connection_string)

table_name = 'city'  
query = f"SELECT * FROM {database}.{table_name}"

chart_df = pd.read_sql(query, engine)

#faq table read
faq_table = 'faq'
faq_query = f'select * from {faq_table}'
faq = pd.read_sql(faq_query, engine)


pages = {
    "Main": [
        st.Page("main.py", title="🏠Home"),
    ],
    "Statistics": [
        st.Page("stats1.py", title="전국 자동차 등록 현황"),
        st.Page("stats2.py", title="전국 인구 밀도 대비 자등차 등록 현황"),
        st.Page("license_stats.py", title="도시별 운전면허 및 차량 밀도 현황"),
    ],
    "FAQ": [
        st.Page("faq.py", title="FAQ")
    ]
}

faq_table = 'faq'
faq_query = f'select * from {faq_table}'
faq = pd.read_sql(faq_query, engine)


pg = st.navigation(pages)
pg.run()
