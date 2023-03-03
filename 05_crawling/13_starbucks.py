from bs4 import BeautifulSoup
from urllib import request

# url = 'https://www.starbucks.co.kr/store/store_map.do'
# re = request.urlopen(url)
# soup = BeautifulSoup(re, 'html.parser')
# print(soup)
# print(soup.select('ul.quickSearchResultBox'))

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(5)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

# print(soup.select('li.quickResultLstCon strong'))
# print(soup.select('li.quickResultLstCon p.result_details'))

