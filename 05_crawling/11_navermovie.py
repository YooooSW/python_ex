import requests
from bs4 import BeautifulSoup
import re

url = 'https://movie.naver.com/movie/point/af/list.naver'
re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')
num = []
title = []
score = []
contents = []

data = soup.select('td.ac.num')
# print(data)
for item in data:
    num.append(item.string.strip())
# print(num)

data = soup.select('a.movie.color_b')
for item in data:
    title.append(item.string.strip())
# print(title)

data = soup.select('div.list_netizen_score em')
# print(data)
for item in data:
    score.append(item.string.strip())
# print(score)

data = soup.select('td.title')
for item in data:
    contents.append(item.get_text(strip=True))
# print(contents)

items = list(zip(num,title,score,contents))
print(items)