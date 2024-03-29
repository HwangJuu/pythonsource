print()

import requests
from fake_useragent import UserAgent
import csv

# 다음 주식 사이트
headers = {"user-agent": UserAgent().chrome, "referer": "https://finance.daum.net/"}
# 다운로드 기본경로
path = "./RPAbasic/crawl/download/"
# 빈 리스트 생성
data = []

try:
    url = "https://finance.daum.net/api/search/ranks?limit=10"
    res = requests.get(url, headers=headers)
    print(res.text)

    rank_json = res.json()["data"]

    for item in rank_json:
        print(
            "순위 {}, 금액 {}, 회사명 {}".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )
        data.append(item)

        with open(path + "finanace.txt", "a", encoding="utf-8") as txt, open(
            path + "finanace.csv", "a", encoding="utf-8", newline=""
        ) as csvfile:

            # 텍스트 저장
            txt.write(
                "순위 {}, 금액 {}, 회사명 {}\n".format(
                    item["rank"], item["tradePrice"], item["name"]
                )
            )

            # csv 저장
            output = csv.writer(csvfile)
            # 헤더명
            output.writerow(data[0].keys())
            for row in data:
                output.writerow(row.values())  # value 저장

except Exception as e:
    print(e)


print()
