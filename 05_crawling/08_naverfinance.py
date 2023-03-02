# import urllib.request
# import urllib.parse as parse
import requests
from bs4 import BeautifulSoup

# url = "https://finance.naver.com/marketindex/"
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html,'html.parser')
# result = soup.select("h3.h_lst > span.blind")
# value = soup.select("span.value")
# while True:
#     select = int(input("금융번호를 입력하세요(0~11): "))
#     for i in range(0, 12):
#         if i == select:
#             print(result[i].string,": ",value[i].string)



url = 'https://finance.naver.com/marketindex/exchangeList.naver'
re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')
name = []
price = []
data = soup.select('td.tit a')

# print(data)
for item in data:
    name.append(item.string.strip())
# print(name)

data = soup.select('td.sale')
for item in data:
    price.append(float(item.string.replace(',','')))
# print(price)
# 묶고자하는데이터를 zip써서 묶어줌
items = list(zip(name,price))
print(items)
