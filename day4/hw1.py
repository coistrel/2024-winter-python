# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/joonggonara/994948311')

time.sleep(1)

element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/div[2]/iframe")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(4)
driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight)", element)
time.sleep(10000)