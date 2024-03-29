print()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
browser.get("http://www.python.org")
browser.maximize_window()

# 결과 페이지에서 원하는 요소 찾기 - 기준 부여
# find_element() : 하나의 요소를 찾을 때
# find_elements() : 여러개의 요소를 찾을 때

# 기준 - By
# By.NAME, By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT,
# By.PARTIAL_LINK_TEXT, By.TAG_NAME, By.XPATH

# 아이디 값으로 찾기
element = browser.find_element(By.ID, "id-search-field")

# css 선택자로 찾기
element = browser.find_element(By.CSS_SELECTOR, "#id-search-field")

# 클래스 이름으로 찾기
element = browser.find_element(By.CLASS_NAME, "search-field")

# Xpath로 찾기 - 복사 필요
element = browser.find_element(By.XPATH, '//*[@id="id-search-field"]')

# 검색 창에 python 입력
element.send_keys("python")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()

print()
