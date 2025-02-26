import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

# 1. request -> url 요청
url=f'http://dartsharing.com/sub_partner.php#cont08'
response=requests.get(url)

# 2. html 응답
html=response.text
# 3. beautifulSoup 객체 생성
bs=BeautifulSoup(html,'html.parser')

# 4.
title = bs.select_one('title')

# 브랜드 추출
if title:
    company_name=title.text.strip()

qa_content=bs.select_one('div.partner_faq.partner_faq01') 
print(qa_content)


qa_content = bs.select('.list00')  # 'list00' 클래스를 가진 모든 요소 선택

q_list = []
a_list = []

# 각 'list00' 요소에 대해 질문과 답변 추출
for item in qa_content:
    question = item.select_one('p.open_list_tit')  # 질문 부분
    time.sleep(2)
    answer = item.select_one('p.open_list_text')  # 답변 부분
    time.sleep(2)
    
    if question and answer:
        q_list.append(question.text.strip())
        time.sleep(2)
        a_list.append(answer.text.strip())
        time.sleep(2)


import mysql.connector 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="030617",
    database="not_temu_project"
)
cursor = conn.cursor()

for question, answer in zip(q_list, a_list):  # zip() 사용
    # SQL 쿼리
    sql = "INSERT INTO faq (vehicle_id,company_name, question, answer) VALUES (%s,%s, %s, %s)"
    cursor.execute(sql, (4,company_name, question, answer))

cursor = conn.cursor()
conn.commit()

cursor.close()
conn.close()
# 회사 이름 변수!!
# company_name