import math
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

limit = 50

search_count_pages_text = indeed_soup.find("div", {"id":"searchCountPages"}).text
# 예시결과: 1페이지 결과 1,466건

count_text = search_count_pages_text.split()
# ['1페이지', '결과', '1,466건']
contents_max_count = count_text[-1:][0]
# 1,467건

contents_max_count = contents_max_count.replace(',','')
# 1467건

contents_max_count = contents_max_count.replace('건','')
# 1467 ->type is str

contents_max_count = int(contents_max_count)
# 1467 ->type is int

max_page_num = math.ceil(contents_max_count/limit)
# 50으로 나누고 올림

print(max_page_num)
