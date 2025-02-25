import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve

class NewsEntry:
    def __init__(self,title,href,img_path):
        self.title=title
        self.href=href
        self.img_path=img_path
    
    # 이건 모에요?
    def __repr__(self):
        return f'NewsEntry<title={self.title},href={self.href},img_path={self.img_path}>'
 

keyword=input("검색 기간:")
url=f"https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=1244&hDivEng=&month_yn="
res=requests.get(url)
html=res.text
bs=BeautifulSoup(html,'html.parser')
sStarts=bs.select('select#sStart.form-control')
for sStart in sStarts:
    print(sStart)
# for news_content in enumerate(news_contents): # enumerate: iterable한 객체를 순회하기 위해서 쓰는 함수->인덱스 번호 가져올 수 있음
#     news_tit=news_content.select_one('a.news_tit')
#     title=news_tit.text
#     href=news_tit['href']
#     img=news_content.select_one('img.thumb')
#     lazysrc=img['data-lazysrc']
#     if lazysrc.startswith('http'):
#         img_dir="/Users/comet39/SKN_bootcamp/WEB_CRAWLING/static-web-page/images"
#         today=datetime.now().strftime('%y%m%d')
#         filename=f'{img_dir}/{today}_{i}.jpg'
#         urlretrieve(lazysrc,filename)

#     news_entry=NewsEntry(title,href,filename)
#     news_list.append(news_entry)


# print(news_list)