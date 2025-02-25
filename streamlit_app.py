import streamlit as st
from sqlalchemy import create_engine
import pandas as pd


username = 'root'  
password = '1092' 
host = 'localhost'  
port = '3306' 
database = 'mydb' 

connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string)

table_name = 'city'  
query = f"SELECT * FROM {table_name}"

chart_df = pd.read_sql(query, engine)

pages = {
    "Main": [
        st.Page("main.py", title="Create your account"),
    ],
    "Statistics": [
        st.Page("stats1.py", title="Statistics Page 1"),
        st.Page("stats2.py", title="Statistics Page 2"),
    ],
    "FAQ": [
        st.Page("faq.py", title="FAQ")
    ]
}


pg = st.navigation(pages)
pg.run()
