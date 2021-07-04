from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
title = soup.select("ul#exchangeList span.value")
f = open("./환율.txt", "w")
for i in title:
    print(i.string)
    f.write(i.string + "\n")
f.close()