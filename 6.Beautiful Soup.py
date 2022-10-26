import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")      # res는 response 번호만 찍히기 때문에, text로 바꿔야 내용을 가져옴
# print(soup.title)             # html에서 해당부분 전체 가져옴
# print(soup.title.get_text())  # 내용만 가져옴 
print(soup.a)                 # 전체 내용 중 첫번째 a를 가져옴
# print(soup.a.attrs)           # 태그의 속성 보여줌
print(soup.a["onclick"])      # 속성 중 지정한 내용만 불러옴

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))   # 해당 속성가진 a 중 첫번째 가져옴
# print(soup.find(attrs={"class":"Nbtn_upload"}))   # 해당 속성가진 a 중 첫번째 가져옴

# print(soup.find("li", attrs={"class":"rank01"}).get_text())
# rank01 = soup.find("li", attrs={"class":"rank01"})
# print(rank01.a.get_text)
# print(rank01.next_sibling.next_sibling)      # 줄바꿈 때문에 두번 기재
# rank02 = rank01.next_sibling.next_sibling  
# rank03 = rank02.next_sibling.next_sibling
# print(rank03.a.get_text())

# print(rank01.parent)

# rank02 = rank01.find_next_sibling("li")  # 줄바꿈 상관없이바로 다름 형제 찾기
# print(rank02.a.get_text())
# rank01 = rank02.find_previous_sibling("li")
# print(rank01.a.get_text())

# print(rank01.find_next_siblings("li"))

# webtoon = soup.find("a", text="전지적 독자 시점-012. Ep.02 주인공 (6)")
# print(webtoon)