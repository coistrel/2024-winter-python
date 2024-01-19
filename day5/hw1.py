from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("https://everytime.kr/")
original_window = driver.current_window_handle
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.switch_to.new_window('tab')
time.sleep(2)
driver.get("https://mdrims.dongguk.edu/")
time.sleep(2)
driver.switch_to.window(original_window)
time.sleep(2)
driver.fullscreen_window()
time.sleep(20)