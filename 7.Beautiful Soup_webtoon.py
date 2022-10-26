import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 요일별 전체 웹툰 가져오기
cartoon = soup.find_all("a", attrs={"class":"title"})   # class 속성이 title인 점을 이용
for ct in cartoon : 
    print(ct.get_text())

