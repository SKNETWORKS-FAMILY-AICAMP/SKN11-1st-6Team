from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import mysql.connector

driver = webdriver.Chrome()  # 또는 다른 브라우저 드라이버
driver.get('https://kmscorp.co.kr/faq_c1-2')
# MySQL 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="030617",
    database="not_temu_project"
)
cursor = conn.cursor()
try:
    # 페이지가 로드될 때까지 기다립니다. (필요한 경우)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'acd_group'))
    )

    # HTML 가져오기
    html = driver.page_source

    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 모든 질문이 들어있는 acd_row div들을 찾습니다.
    question_wrappers = soup.find_all('div', class_='acd_row')

    # 각 질문 wrapper에서 질문과 답변을 추출합니다.
    for wrapper in question_wrappers:
        # 질문 추출
        question_element = wrapper.find('span', class_='table-cell')
        question_text = question_element.text.strip() if question_element else "질문 없음"

        # 답변 추출
        answer_element = wrapper.find('div', class_='board_contents fr-view')
        answer_text = answer_element.text.strip() if answer_element else "답변 없음"
        sql = "INSERT INTO faq (vehicle_id, company_name, question, answer) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (1, '카카오T 블루', question_text, answer_text))

except Exception as e:
    print(f"오류 발생: {e}")

conn.commit()
cursor.close()
conn.close()

