from selenium import webdriver
import time
import chromedriver_autoinstaller

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(2)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(2)

browser.switch_to.frame(browser.find_element_by_css_selector("#down"))
# 중고나라 게시판 클릭
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(2)

try:
	f = open("./중고나라.txt", "r", encoding="utf-8")
	ref = f.readlines()
except:
	f = open("./중고나라.txt", "w")
	ref = []
f.close()

# 중고나라 게시판 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
	if (i.text+"\n") not in ref: # 최신에 올라온 글이라면?
		f = open("./중고나라.txt", "a", encoding="utf-8")
		f.write(i.text + "\n")
		f.close()
		if "선풍기" in i.text: # 내가 관심있어할 물건이라면?
			new_one += 1

print(f"선풍기 관련 글이 {new_one}개 올라왔습니다.")
browser.close()

if new_one >= 1:
	from twilio.rest import Client

	account_sid = "ACefe43744d5ca8b39d239f2a622c277e0"
	auth_token = "7de23e489e3bb3303d728e97783d57a1"
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
						 body=f"선풍기 관련 글이 {new_one}개 올라왔습니다.   https://cafe.daum.net/talingpython/rRa6",
						 from_='+14703090526',
						 to='+821095518905'
					 )
