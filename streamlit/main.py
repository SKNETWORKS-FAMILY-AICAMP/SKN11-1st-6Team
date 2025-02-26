import streamlit as st

# 사용자 정의 CSS 적용
st.markdown(
    """
    <style>
        /* 전체 페이지 배경색 */
        .main {
            background-color: #f4f4f4;
        }

        /* 제목 스타일 */
        .title {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #333;
        }

        /* 부제목 스타일 */
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }

        /* 기능 카드 스타일 */
        .feature-card {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            margin-bottom: 20px;
        }

        /* 버튼 스타일 */
        .stButton>button {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #5a7ae0, #8f5fd1);
        }

        /* 팀원 소개 스타일 */
        .team-card {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }

        .team-img {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            object-fit: cover;
            margin-bottom: 10px;
        }

        .team-name {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .team-role {
            font-size: 14px;
            color: #777;
        }
        
        
        /* 주요 기능 박스 스타일 */
        .feature-card {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            margin-bottom: 20px;
            min-height: 150px; /* 박스 크기 고정 */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 메인 제목 및 설명
st.markdown("<h1 class='title'>🚗 Mobility Link</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>이동수단 최적 배치를 위한 데이터 분석 플랫폼</p>", unsafe_allow_html=True)

st.write("모빌리티의 최적 배치를 위해 국내 지역별 자동차 등록 현황과")
st.write("인구 밀도 관련 정보 및 분석 자료를 제공합니다!")   
st.write("화면 좌측의 사이드바를 통해 원하는 정보를 얻어보세요!!")

st.write("")  # 공백 추가

# 주요 기능 섹션
st.subheader("🚀 주요 기능")
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class='feature-card'>
            <a href="/stats1" class="feature-link"><h4>전국 자동차 등록 현황</h4></a>
            <p>전국의 시도별 자동차 등록 현황 분석</p>
            
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class='feature-card'>
            <a href="/stats2" class="feature-link"><h4>도시별 차량 밀도 분석</h4></a>
            <p>도시별 차량 밀도를 한눈에 확인</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
with col2:
    st.markdown(
        """
        <div class='feature-card'>
            <a href="/license_stats" class="feature-link"><h4>인구 대비 자동차 등록 현황</h4></a>
            <p>인구 밀도 대비 자동차 등록 현황을 분석하여 효율적인 이동수단 배치</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class='feature-card'>
            <a href="/faq" class="feature-link"><h4>FAQ</h4></a>
            <p>자주 묻는 질문과 상세 가이드</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")  # 공백 추가

# # 팀원 소개
# st.markdown("<h2 class='subtitle'>👥 팀원 소개</h2>", unsafe_allow_html=True)

# team_members = [
#     {"name": "황준호", "role": "ENTJ", "image": "../이미지/image-1.png"},
#     {"name": "김한솔", "role": "ESFJ", "image": "../이미지/image.png"},
#     {"name": "정현욱", "role": "ISTP", "image": "../이미지/image-2.png"},
#     {"name": "오정현", "role": "ISTP", "image": "../이미지/image-3.png"},
#     {"name": "이혜성", "role": "ISFJ", "image": "../이미지/image-4.png"},
# ]

# cols = st.columns(len(team_members))

# for col, member in zip(cols, team_members):
#     with col:
#         st.markdown(
#             f"""
#             <div class='team-card'>
#                 <img class='team-img' src="{member['image']}" alt="{member['name']}">
#                 <p class='team-name'>{member['name']}</p>
#                 <p class='team-role'>{member['role']}</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
st.write('')
st.write('')
st.markdown("<h2 class='subtitle'>👥 팀원 소개</h2>", unsafe_allow_html=True)

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

