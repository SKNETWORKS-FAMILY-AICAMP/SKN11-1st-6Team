from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector

# Chrome 실행
driver = webdriver.Chrome()

# 특정 URL 접근
driver.get('https://gcoo.io/startup#faq')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@name="Question Wrapper"]')))

# "Question Wrapper" 요소 찾기
wrapper = driver.find_element(By.XPATH, '//div[@name="Question Wrapper"]')

# 토글 버튼 가져오기 (질문을 펼칠 버튼)
toggle_buttons = wrapper.find_elements(By.CSS_SELECTOR, "div.framer-ze9euj")
print(f"찾은 토글 버튼 개수: {len(toggle_buttons)}")

# 모든 질문 펼치기
for btn in toggle_buttons:
    try:
        ActionChains(driver).move_to_element(btn).click().perform()
        time.sleep(1)  # 버튼 클릭 후 잠깐 대기
        driver.execute_script("window.scrollBy(0, 150);")  # 부드럽게 스크롤
        time.sleep(1)
    except Exception as e:
        print(f"클릭 실패: {e}")

# 질문과 답변 가져오기
questions = []
answers=[]

# 모든 질문과 답변 요소 가져오기
a_elements = wrapper.find_elements(By.CLASS_NAME, 'framer-19tie9q')
q_elements = wrapper.find_elements(By.CLASS_NAME, 'framer-zzvis2')

for q in q_elements:
    try:
        text = q.text.strip()
        if text:  # 빈 텍스트는 제외
            questions.append(text)
    except Exception as e:
        print(f"텍스트 가져오기 실패: {e}")

for a in a_elements:
    try:
        text = a.text.strip()
        if text:  # 빈 텍스트는 제외
            answers.append(text)
    except Exception as e:
        print(f"텍스트 가져오기 실패: {e}")

# 브라우저 종료
driver.quit()

# 질문과 답변 개수 확인 후, 불일치하면 조정
if len(questions) != len(answers):
    # print("⚠️ 질문과 답변 개수가 맞지 않습니다. 데이터 정리 필요.")
    questions = questions[:len(answers)]  # 불일치하면 길이를 맞춤

# MySQL 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="030617",
    database="not_temu_project"
)
cursor = conn.cursor()

# 데이터 삽입
for question, answer in zip(questions, answers):
    sql = "INSERT INTO faq (vehicle_id, company_name, question, answer) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (4, '지쿠', question, answer))

conn.commit()
cursor.close()
conn.close()

print("✅ MySQL 데이터 삽입 완료")
