from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
search = input("검색어: ")
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+search)
time.sleep(4)
imgs = driver.find_elements(By.CLASS_NAME,'_fe_image_tab_content_thumbnail_image')
for i,j in enumerate(imgs):    
    src = j.get_attribute("src")
    if "base64" not in src:
        request.urlretrieve(src, f"//img//{i}.jpg")
    