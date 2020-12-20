from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import requests
from naver_login import login
from naver_note import send_note
import sqlite3


#네이버 로그인
login('sunsart9', 's05130322')

#sqlite3
conn = sqlite3.connect('naver_id.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS naver(name text)')

try:
    driver = webdriver.Chrome()
    for i in range(1, 6):   #네이버카페 검색 / 5페이지까지 / 키워드:김포 / 영역:제목 / 등록기간:1일 / 정확도순
        driver.get('https://cafe.naver.com/ca-fe/home/search/articles?q=%EA%B9%80%ED%8F%AC&p=' + str(i) + '&se=1&pr=1')
        driver.implicitly_wait(3)

        for j in range(1, 2):
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div/div[3]/ul/li[' + str(j) + ']/div/div/div/a').click()

            #새로 열린 탭으로 전환
            driver.switch_to.window(driver.window_handles[-1])

            #새탭 열기 로딩 기다리기
            time.sleep(2)

            #새로 열린 탭의 게시물의 iframe 전환
            driver.switch_to.frame("cafe_main")

            #카페 게시물에서 글쓴이의 아이디 추출
            soup = bs(driver.page_source, 'html.parser')
            a = soup.find('a', {'class':'nickname'})
            naver_id = a['id'][10:]

            #데이터베이스에 저장
            sql = 'INSERT INTO naver (name) VALUES (?)'
            cursor.execute(sql, (naver_id,))
            conn.commit()           

            #
            # cursor.execute("SELECT * FROM naver")
            # ids = cursor.fetchall()

            # for id in ids:
            #     if(id[0] == naver_id):
            #         print('중복됨, 저장안함, 쪽지발송안함')
            #     else:
            #         print('중복안됨, 저장함, 쪽지발송함')
            #         cursor.execute('INSERT INTO naver VALUES(naver_id)')
            #         conn.commit()
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    conn.close()
except Exception as e:
    print('네이버카페 검색과정에서 에러발생')
    print(e)