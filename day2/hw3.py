import re
import requests
from bs4 import BeautifulSoup as bs
art = []
song = []
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
response = requests.get("https://www.melon.com/chart/index.htm", headers=header)
soup = bs(response.text, 'html.parser')

#img의 src 출력
for j in soup.select("#lst50 > td:nth-child(4) > div > a > img"):
    print(j["src"])

for i in soup.select("#lst50 > td > div > div > div.ellipsis.rank01 > span > a"):
    song.append(i.text)
for i in soup.select("#lst50 > td > div > div > div.ellipsis.rank02 > a"):
    art.append(i.text)
patt = re.compile('아이.')
for i in range(len(song)):
    if patt.findall(art[i]):
        print(song[i], "-", art[i])