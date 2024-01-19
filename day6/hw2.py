#kda.xlsx 
#시간 챔프 k d a

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

wb = load_workbook('kda.xlsx',read_only=False, data_only=False)
sheet1 = wb['Sheet1']
nic = "닉네임뭐로해야함"
# nic = input("닉 : ")
driver.get('https://www.op.gg/summoners/search?q='+nic+'&region=kr')
time.sleep(1)

for i in range(1,6):
        kda = driver.find_elements(By.XPATH, f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span')
        cmp = driver.find_element(By.XPATH, f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[2]/div[1]/div[1]/a/img').get_attribute('alt')
        day = driver.find_element(By.XPATH, f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[1]/div[1]/div[2]/div').text
        # print(cmp, day, kda[0].text ,kda[1].text, kda[2].text)
        sheet1[f'A{i+1}'].value = cmp
        sheet1[f'B{i+1}'].value = day
        sheet1[f'C{i+1}'].value = kda[0].text
        sheet1[f'D{i+1}'].value = kda[1].text
        sheet1[f'E{i+1}'].value = kda[2].text
wb.save(filename="kda.xlsx")
# try:
#     b = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[2]/ul/li[1]/a')
#     b.click()
#     time.sleep(100)
    
# except:
#     print("NONE")