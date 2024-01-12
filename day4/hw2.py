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
driver.switch_to.frame("cafe_main")
header = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]")
driver.execute_script('arguments[0].innerHTML = "저눙현"',header)

time.sleep(111)