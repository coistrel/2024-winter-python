# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from openpyxl import load_workbook

driver = webdriver.Chrome()

wb = load_workbook('study.xlsx',read_only=False, data_only=False)
sheet1 = wb['Sheet1']
get_cells = sheet1['B2':'B3001']
for i in range(2, 23):
    word = sheet1[f'B{i}'].value
    driver.get('https://en.dict.naver.com/#/search?query='+word+'&range=word')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="searchPage_entry"]/div/div[1]/div[1]/a').click()
    time.sleep(1)
    p = driver.find_element(By.CLASS_NAME, 'pronounce')
    sheet1[f'E{i}'].value = p.text
    # print(f"{i} : {word} {p.text}")

wb.save(filename='study.xlsx')