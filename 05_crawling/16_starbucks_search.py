from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://www.starbucks.co.kr/store/store_map.do'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

loca = driver.find_element(By.CLASS_NAME,'loca_search')
loca.click()
time.sleep(5)

sido = driver.find_elements(By.CSS_SELECTOR,'ul.sido_arae_box > li')
# print(sido)
sido[0].click()
time.sleep(5)

gugun = driver.find_elements(By.CSS_SELECTOR,'ul.gugun_arae_box > li')
# print(sido)
sido[1].click()
time.sleep(5)

# print(soup.select('li.quickResultLstCon strong'))
# print(soup.select('li.quickResultLstCon p.result_details'))