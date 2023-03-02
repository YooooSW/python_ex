from urllib import request
url = 'https://washenjoy.co.kr/wp-content/uploads/2021/02/%EA%B2%A8%EC%9A%B8%EC%98%B7%EC%99%B8%ED%88%AC%EA%B4%80%EB%A6%AC%EB%B0%A9%EB%B2%9510.jpg'
filename = '05_crawling/down/겨울.jpg'
request.urlretrieve(url,filename)

print('down')