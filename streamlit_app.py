import streamlit as st
import test

test.run_data_preprocessing_and_insert()

pages = {
    "Main": [
        st.Page("main.py", title="Create your account"),
    ],
    "Statistics": [
        st.Page("stats.py", title="Statistics Page 1"),
        st.Page("stats2.py", title="Statistics Page 2"),
    ],
}

pg = st.navigation(pages)
pg.run()
