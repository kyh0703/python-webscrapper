import requests

r = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
print(r.text)