print()
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.daum.net")
browser.maximize_window()

print(browser.current_url)  # https://www.daum.net/
print(browser.title)  # Daum

# 브라우저 타이틀 안에 Daum이 없다면 오류를 발생시킴
# 테스트 코드에서 오류가 발생하면 이후 코드는 실행 안함
assert "Daum" in browser.title

# 현재 페이지 소스 가져오기
print(browser.page_source)

# 세션 id 가져오기
print(browser.session_id)

# 쿠키 정보 가져오기
print(browser.get_cookies)

time.sleep(3)
browser.quit()

print()
