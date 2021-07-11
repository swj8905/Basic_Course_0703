from selenium import webdriver
import time
import chromedriver_autoinstaller
import random

hash_tag = input("해시태그 입력 >> ")

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
# 로그인 하기
id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson") # 본인 아이디 적어주세요.
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3!@#") # 본인 비밀번호 적어주세요.
button = browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()
time.sleep(5)

# 해시태그 검색
url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(url)
time.sleep(5) # 혹시 이쯤에서 에러나시는 분들은 얘를 6~7초로 바꿔보세요.

# 첫번째 사진 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0") # 이게 안되시는 분들은 "div.KL4Bh" <-- 이거 한번 써보세요.
first_photo.click()
time.sleep(4)

# 자동 좋아요 시작
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
    if value == "좋아요": # 좋아요가 안눌려있다면?
        like.click()
        # time.sleep(random.randint(30, 40) + random.random())
        next.click()
        # time.sleep(random.randint(30, 40) + random.random())
        time.sleep(3)
    elif value == "좋아요 취소": # 좋아요가 눌려있다면?
        next.click()
        # time.sleep(random.randint(30, 40) + random.random())
        time.sleep(3)
