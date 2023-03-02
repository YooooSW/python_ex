import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')
title = []
artist = []

data = soup.select('p.title a')
# print(data)
for item in data:
    title.append(item.string.strip())
# print(title)

data = soup.select('p.artist a')
# print(data)
for item in data:
    artist.append(item.string.strip())
# print(artist)
items = list(zip(title,artist))
print(items)