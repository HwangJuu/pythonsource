print()
# gmarket best - 컴퓨터/전자 항목 추출

import requests
from bs4 import BeautifulSoup

url = "http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 1위 ~ 100위 아이템 찾기
# div.best-list li : li는 자손의 개념
best_list = soup.select("div.best-list li")

for idx, item in enumerate(best_list):
    # 상품명
    title = item.select_one("a.itemname")
    # 가격
    price = item.select_one("div.s-price span").get_text()

    # 순위, 상품명, 가격, 상품상세정보 url
    # print(idx + 1, title.get_text(), price, title["href"])

    # title["href"] 를 이용해서 requests.get() 요청
    # 상세 주소 이용
    product_url = title["href"]
    res = requests.get(title["href"])
    detail_soup = BeautifulSoup(res.text, "lxml")

    # 회사명 추출(회사명 없으면 셀러명 추출)
    company = detail_soup.select_one("span.text__brand > span.text")

    # 제조사가 없는 경우 셀러명 추출
    # 12번이 제조사가 없음
    # eletment를 못찾았는데 get_text()를 호출 : AttributeError: 'NoneType' object has no attribute 'get_text'
    if not company:
        company = detail_soup.select_one("span.text__seller > a")

    # 최종 : 순위, 상품명, 가격, 회사명, 상품상세정보 url
    print(idx + 1, title.get_text(), price, company.get_text(), product_url)


print()
