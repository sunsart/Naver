from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import requests

try:
    #네이버카페 검색 / 키워드:김포 / 영역:제목 / 등록기간:1일 
    driver = webdriver.Chrome()
    url = 'https://cafe.naver.com/ca-fe/home/search/articles?q=%EA%B9%80%ED%8F%AC&se=1&pr=1'
    driver.get(url)
    driver.implicitly_wait(3)

    html = driver.page_source
    soup = bs(html, 'html.parser')

    list = soup.select('.article_item')
    print(list[0])

    #for article in articles:
    #    print(article.get_text())
 

except Exception as e:
    print('네이버카페 검색과정에서 에러발생')
    print(e)