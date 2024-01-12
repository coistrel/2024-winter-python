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
# driver.switch_to.frame("cafe_main")
ifr = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/div[2]/iframe")
driver.execute_script('arguments[0].setAttribute("src","https://hianna.tistory.com/480");',ifr)

time.sleep(1000)