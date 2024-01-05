import requests
from bs4 import BeautifulSoup
url = "https://search.naver.com/search.naver"
v = input("검색어: ")
p = {"query": v}
response = requests.get(url, params=p)
soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

for i in soup.select('.news_contents > a'): #css selector 사용
    print(i.text) #글 출력
    print(i['href']) #a 태그 내 href 속성 출력