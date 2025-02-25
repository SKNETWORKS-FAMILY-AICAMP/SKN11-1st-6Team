#동적 페이지 웹 스크래핑 -> selenium
#인증을 요구하는 특정 웹 페이지의 데이터 스크랩
#무한 댓글 스크랩
#브라우저용 매크로로써 사용 가능
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 웹드라이버 실행 (Chrome 브라우저 열기)
driver = webdriver.Chrome()  # ()를 추가하여 인스턴스 생성

# url 접속
url='https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=1244&hDivEng=&month_yn='
driver.get(url)
# time.sleep(1)

# 요소 접근
start_elems=driver.find_element(By.ID,'sStart')
    
# Select 객체 생성
select = Select(start_elems)

# 값 선택
year=input("검색 기간을 입력하세요.")
select.select_by_value(year)

# 검색 버튼 찾기 및 클릭
search_button = driver.find_element(By.CSS_SELECTOR, "button.mu-btn.mu-btn-secondary")
search_button.click()

# 데이터추출
# table = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "sheet-frame"))
# )
# table = driver.find_element(By.ID, "sheet01-table")
# time.sleep(5)
# print("확인")


# date_element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'HideCol0C1')]"))
#     # EC.presence_of_element_located((By.XPATH, "//*[@id=\"sheet01-table\"]/tbody/tr[2]/td[1]/div/div[6]/table/tbody/tr[5]/td[2]"))
# )
date_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.GMClassReadOnly.GMWrap0.GMText.GMCell.IBSheetFont0.HideCol0C1"))
    <td style="background-color:rgb(201,225,245);" class=" GMClassReadOnly GMWrap0 GMText GMCell IBSheetFont0 HideCol0C1" colspan="2">2022-01</td>
    )

date_text = date_element.text
print(date_text)

region_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'HideCol0C2')]"))
)
region_text = region_element.text
print(region_text)
#
# for col in (cols[0]):
#     row = col.find_elements(By.TAG_NAME, "td")
#     time.sleep(1)
#     print([col.text for col in cols])


# 브라우저 종료
driver.quit()
