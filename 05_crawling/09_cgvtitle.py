import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')
title = []
data = soup.select('strong.title')

# print(data)
for item in data:
    # title.append(item.string.strip())
    print(item.string)
# print(title)

