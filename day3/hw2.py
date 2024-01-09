#캡스 홈페이지에 로그인 한 후, 캡스 위키(UTIL → CAPS 위키 클릭)에 접속하여 검색한 결과값을 불러온 후,
# 파일 입출력을 통해 결과값.txt로 저장하세요.

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
driver.get('http://capszzang.gq/')
time.sleep(0.1)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[6]/a').click() #로그인 창 클릭
time.sleep(0.1)
driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('haeli1') #아이디 입력
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('wh1340170') #패스워드 입력
driver.find_element(
    By.XPATH, '/html/body/section[2]/div/div/div/form/div[3]/button').click()  # 로그인 버튼 클릭
time.sleep(0.1)
try: #예외처리
    result = driver.switch_to.alert #alert창으로 전환
    result.accept() #alert 확인 버튼 클릭
except:
    pass
time.sleep(0.1)

driver.find_element(
    By.XPATH, '/html/body/header/div/nav/div/ul/li[5]/a').click()
driver.find_element(
    By.XPATH, '/html/body/header/div/nav/div/ul/li[5]/div/ul/li[3]/a').click()
search = input("검색어: ")
driver.find_element(
    By.XPATH, '/html/body/section[2]/div[1]/form/input').send_keys(search)
driver.find_element(By.XPATH, '/html/body/section[2]/div[1]/form/button').click()

content = driver.find_elements(By.XPATH, '/html/body/section[3]/div')

f = open("./2024-winter-python/day3/result.txt", "w")
for i in content:
    f.write(i.text)