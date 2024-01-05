#네이버 증권의 인기 검색 종목의 순위, 종목명, 현재가, 등락률, PER를 출력해 주세요.

import requests
from bs4 import BeautifulSoup as bs
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
response = requests.get("https://finance.naver.com/sise/lastsearch2.naver")
soup = bs(response.text, 'html.parser')
for i in soup.select("#contentarea > div.box_type_l .type_5 tr"):

        try:
                no = i.select(".no")
                title = i.select(".tltle")
                curr = i.select("td:nth-child(4)")
                fr = i.select("td:nth-child(6)")
                PER = i.select("td:nth-child(11)")
                print(no[0].text, title[0].text, curr[0].text, fr[0].text.strip(), PER[0].text, sep="\t")
                
        except:
                continue   