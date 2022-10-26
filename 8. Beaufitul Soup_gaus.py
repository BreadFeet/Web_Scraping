import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()    # test용으로 첫번째 값의 a element의 텍스트 가져오기
# link = cartoons[0].a["href"]        # a 태그의 속성은 []로 불러올 수 있음
# print(title)
# print("https://comic.naver.com/"+link)  # 바로 연결해야 하므로 ,는 안됨!

# 만화정보와 링크 가져오기
# for cartoon in cartoons :
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+cartoon.a["href"]
#     print(title, link)

# 평점 정보 가져오기
# total_rates = 0
scores = soup.find_all("div", attrs={"class":"rating_type"})
# for score in scores :
#     rate = score.find("strong").get_text()
#     print(rate)
#     total_rates += float(rate)           # print(type(rate)): str

# # 평점 평균 구하기
# print("전체 평점 합:", total_rates)
# print("평균 평점:", total_rates/len(scores))

# strong을 바로 찾아서 get_text()로 평점을 불러올 수 있을까? NO
scores = soup.find_all("strong")
print(scores)


