#캡스 집행부원을 출력해 주세요. (ABOUT → CAPS 집행부 소개)

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
time.sleep(1)
driver.find_element(
    By.XPATH, '/html/body/header/div/nav/div/ul/li[1]/a').click() #로그인 창 클릭
time.sleep(0.1)
driver.find_element(
    By.XPATH, '/html/body/header/div/nav/div/ul/li[1]/div/ul/li[4]/a').click() #로그인 창 클릭
time.sleep(0.1)


nickname = driver.find_elements(
        By.XPATH, '/html/body/section/div//ul/li/a[2]') #닉네임 정보 알아오기
for i in nickname:
    print(i.text)