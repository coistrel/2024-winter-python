from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.
import time

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options) #크롬 열기
time.sleep(2) #2초 대기
driver.get('http://capszzang.gq') # 해당 웹사이트로 접속

# driver.back() #뒤로가기
# driver.forward() #앞으로가기
# driver.refresh() #새로고침

# title = driver.title #페이지 제목
# url = driver.current_url
# handle = driver.current_window_handle

# driver.close()    # 탭 종료
# driver.quit()    # 콘솔까지 완전 종료