# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
driver.get('https://finance.naver.com/sise/lastsearch2.naver')
time.sleep(0.1)
name = driver.find_elements(
    By.XPATH, '//*[@id="contentarea"]/div[3]/table/tbody//tr/td[2]')
curr = driver.find_elements(
    By.XPATH, '//*[@id="contentarea"]/div[3]/table/tbody//tr/td[4]')
fr = driver.find_elements(
    By.XPATH, '//*[@id="contentarea"]/div[3]/table/tbody//tr/td[6]')
per = driver.find_elements(
    By.XPATH, '//*[@id="contentarea"]/div[3]/table/tbody//tr/td[11]')

for i in range(len(name)):
    print(i+1, name[i].text, curr[i].text, fr[i].text, per[i].text)
