# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import pyperclip

from bs4 import BeautifulSoup as bs
import requests

#google 에서 'beautiful 검색창' 으로 검색하기

try:
    #네이버카페 검색 / 키워드:김포 / 영역:제목 / 등록기간:1일 
    URL = 'https://cafe.naver.com/ca-fe/home/search/articles?q=%EA%B9%80%ED%8F%AC&se=1&pr=1'
    result = requests.get(URL)
    html = result.text
    soup = bs(html, "html.parser")
    print(soup)


    #list = soup.select('a.item_subject')
    #print(len(list))

    #for article in articles:
    #    print(article.get_text())
 

except Exception as e:
    print('네이버카페 검색과정에서 에러발생')
    print(e)