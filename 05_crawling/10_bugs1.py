from urllib import request
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
re = request.urlopen(url)
soup = BeautifulSoup(re, 'html.parser')
title = []
artist = []

data = soup.select('p.title > a')
for item in data:
    print(item.string)
    title.append(item.string)

data = soup.select('p.artist > a')
for item in data:
    print(item.string)
    artist.append(item.string.strip())

result = list(zip(title,artist))
print(result)