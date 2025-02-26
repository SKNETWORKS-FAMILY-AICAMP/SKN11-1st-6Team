import streamlit as st
from streamlit_app import chart_df

st.title("🚗MobilityLink")

st.html("<h1 style='font-size: 21px; text-align: left;'>이동수단 최적 배치를 위한 데이터 분석</h1>")
st.write("모빌리티의 최적 배치를 위해 국내 지역별 자동차 등록 현황과")
st.write("인구 밀도 관련 정보 및 분석 자료를 제공합니다!")   
st.write("화면 좌측의 사이드바를 통해 원하는 정보를 얻어보세요!!")
st.write('')
st.subheader('주요 기능')
st.write('✅전국 자동차 등록 현황 페이지: 전국의 시도별 자동차 등록 현황과 인구 밀도 확인📈')
st.write('✅전국 인구 밀도 대비 자동차 등록 현황: 전국의 인구 밀도 대비 자동차 등록 현황 분석📉')
st.write('🚀FAQ 페이지: 자주 묻는 질문 모음')

st.write('')
st.write('')
st.html("<h1 style='font-size: 22px; text-align: left;'>팀원 소개</h1>")

cl1, cl2, cl3, cl4, cl5 = st.columns(5)
col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment="bottom")

with cl1:
    st.html("<h1 style='font-size: 15px; text-align: center;'>황준호</h1>")

with cl2:
    st.html("<h1 style='font-size: 15px; text-align: center;'>김한솔</h1>")

with cl3:
    st.html("<h1 style='font-size: 15px; text-align: center;'>정현욱</h1>")

with cl4:
    st.html("<h1 style='font-size: 15px; text-align: center;'>오정현</h1>")

with cl5:
    st.html("<h1 style='font-size: 15px; text-align: center;'>이혜성</h1>")

with col1:
    st.image('../이미지/image-1.png', caption="ENTJ", use_container_width=True)

with col2:
    st.image('../이미지/image.png', caption="ESFJ", use_container_width=True)

with col3:
    st.image('../이미지/image-2.png', caption="ISTP", use_container_width=True)

with col4:
    st.image('../이미지/image-3.png', caption="ISTP", use_container_width=True)

with col5:
    st.image('../이미지/image-4.png', caption="ISFJ", use_container_width=True)

