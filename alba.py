import os
import csv
import requests
from bs4 import BeautifulSoup as bs

os.system("clear")
alba_url = "http://www.alba.co.kr"


def extract_super_brand_pages():
    result = requests.get(alba_url)
    soup = bs(result.text, "html.parser")
    brand = soup.find("div", {"id": "MainSuperBrand"})
    pages = []
    for a in brand.find_all("a", {"class": "brandHover"}):
        page = dict()
        page["company"] = a.get_text().replace("브랜드채용관 >", "")
        page["link"] = a.get("href")
        pages.append(page)
    return pages


def extract_job_from_brand(page):
    result = requests.get(page)
    soup = bs(result.text, "html.parser")
    tables = (
        soup.find("div", {"class", "goodsList goodsJob"}).find("tbody").find_all("td")
    )
    jobs = []
    count = 0
    types = {0: "region", 1: "title", 2: "time", 3: "pay", 4: "register"}
    job = dict()
    for td in tables:
        v = td.get_text().strip().replace("\xa0", " ").split("\n")
        count += 1
        if count % 6 == 0:
            jobs.append(job.copy())
            job.clear()
        else:
            job[types[(count + 4) % 5]] = "".join(v)
    return jobs


def save_to_file(company, jobs):
    file = open(f"{company}.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        print(list(job.values()))
        writer.writerow(list(job.values()))


pages = extract_super_brand_pages()
for page in pages:
    company = page["company"]
    jobs = extract_job_from_brand(page["link"])
    save_to_file(company, jobs)
