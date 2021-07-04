from bs4 import BeautifulSoup
import urllib.request as req


# 서버한테 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 가져오게 하기
# title = soup.select_one("strong.title")
title = soup.select("div.sect-movie-chart strong.title")

# 요소 내용 출력하기
f = open("./무비차트.txt", "w") # "w" 모드 : 쓰기모드 / "a" 모드 : 더해서 쓰기모드
for i in title:
    # print(i.string)
    f.write(i.string + "\n")
f.close()



