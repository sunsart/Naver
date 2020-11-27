from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import requests

try:
    #네이버카페 검색 / 키워드:김포
    driver = webdriver.Chrome()
    url = 'https://cafe.naver.com/ca-fe/home/search/articles?q=%EA%B9%80%ED%8F%AC'
    driver.get(url)
    driver.implicitly_wait(3)
    
    #영역:제목 / 등록기간:1일 
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/ul/li[2]/div').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[2]/div').click()

    #
    html = driver.page_source
    soup = bs(html, 'html.parser')

    #
    list = soup.select('.item_subject')
    for a in list:
        req = requests.get(a['href'])
        text = req.text
        soup2 = bs(text, 'html.parser')


        div = soup2.find('div', class_='profile_info')
        print(div)
        #a = div.find('a', class_='nickname')
        #print(a.text)
 

except Exception as e:
    print('네이버카페 검색과정에서 에러발생')
    print(e)