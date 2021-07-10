from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://www.youtube.com/watch?v=95ULYjyiFLQ")
time.sleep(5)

# 스크롤 내리기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # 살짝 내리기 # 스크롤 끝까지 내리고 싶으면 : Keys.END
time.sleep(4)
comments = browser.find_elements_by_css_selector("#content-text")

idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("====== 크롤링 끝 ======")
        break
    idx += 1
    if idx % 20 == 0:
        # 새로운 댓글 불러오기 (마우스 스크롤 내려주기)
        browser.find_element_by_css_selector("html").send_keys(Keys.END) # 스크롤 끝까지 내려주기
        time.sleep(5)
        comments = browser.find_elements_by_css_selector("#content-text")