import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())