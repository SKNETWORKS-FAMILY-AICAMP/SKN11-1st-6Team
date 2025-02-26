import streamlit as st
from sqlalchemy import create_engine
import pandas as pd


username = 'root'  
password = '030617' 
host = 'localhost'  
port = '3306' 
database = 'not_temu_project' 

connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string)

table_name = 'city'  
query = f"SELECT * FROM {table_name}"

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
        st.Page("license_stats.py", title="나에게 맞는 창업 도시는?"),
    ],
    "FAQ": [
        st.Page("faq.py", title="FAQ")
    ]
}



pg = st.navigation(pages)
pg.run()
