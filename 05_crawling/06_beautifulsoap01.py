html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_doc = """<img class="" src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readtop_2021_90469_16117848624516236.jpg" data-src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readtop_2021_90469_16117848624516236.jpg" orgwidth="4032" orgheight="3024" alt="사진설명">
<img class="" src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readmed_2021_90469_16117848634516237.jpg" data-src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readmed_2021_90469_16117848634516237.jpg" orgwidth="1000" orgheight="666" alt="사진설명">
<img class="" src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readbot_2021_90469_16117848654516239.jpg" data-src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readbot_2021_90469_16117848654516239.jpg" orgwidth="2800" orgheight="1600" alt="사진설명">
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.p)
# print(type(soup.title))
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.text)
# print(soup.b.parent.name)
# print(soup.p['class'])
# print(soup.a['href'])
# print(soup.a['id'])
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.find(id='link3'))
# print(soup.find(href='http://example.com/tillie'))
# print(soup.find(class_='sister'))


soup.find_all('img')
for link in soup.find_all('img'):
    print(link.get('src'))
# https://washenjoy.co.kr/wp-content/uploads/2021/02/%EA%B2%A8%EC%9A%B8%EC%98%B7%EC%99%B8%ED%88%AC%EA%B4%80%EB%A6%AC%EB%B0%A9%EB%B2%9510.jpg
# <img class="" src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readtop_2021_90469_16117848624516236.jpg" data-src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readtop_2021_90469_16117848624516236.jpg" orgwidth="4032" orgheight="3024" alt="사진설명">
# <img class="" src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readmed_2021_90469_16117848634516237.jpg" data-src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readmed_2021_90469_16117848634516237.jpg" orgwidth="1000" orgheight="666" alt="사진설명">
# <img class="" src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readbot_2021_90469_16117848654516239.jpg" data-src="https://wimg.mk.co.kr/meet/neds/2021/01/image_readbot_2021_90469_16117848654516239.jpg" orgwidth="2800" orgheight="1600" alt="사진설명">




