# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://finance.naver.com/sise/lastsearch2.naver')

# 아이프레임을 대상으로 드라이버 전환하여 상호작용
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.TAG_NAME, 'button').click()

# 이름 또는 ID를 사용하여 전환
driver.switch_to.frame('buttonframe')

# 인덱스를 사용하여 전환
iframe = driver.find_elements(By.TAG_NAME,'iframe')[1]
driver.switch_to.frame(iframe)

# iFrame 나가 기본 콘텐츠로 돌아가기
driver.switch_to.default_content()