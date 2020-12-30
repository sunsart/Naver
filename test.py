from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pyperclip

#일정 이벤트 발생시까지 대기하는 코드
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as bs
import requests
import sqlite3

#-------------------------------------------------------------------

##### 네이버 로그인 #####
id = 'sunsart9'
pw = 's05130322'
try:
    #에러코드 제거하기 위해 : usb_device_handle_win.cc:1020 Failed to read descriptor from node connection:  시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get('https://nid.naver.com/nidlogin.login')
    time.sleep(2)

    pyperclip.copy(id)
    driver.find_element_by_name('id').send_keys(Keys.CONTROL, 'v')
    time.sleep(np.random.rand())    #기계적인 입력에 의한 캡챠를 피하기 위해 랜덤시간만큼 간격을 줌

    pyperclip.copy(pw)
    driver.find_element_by_name('pw').send_keys(Keys.CONTROL, 'v')
    time.sleep(np.random.rand())

    driver.find_element_by_id('log.login').click() 
    time.sleep(2)
    print('네이버 로그인 성공')
except Exception as e:
    print('네이버 로그인 과정에서 에러발생')
    print(e)
##### 네이버 로그인 #####


##### 네이버 쪽지 발송 함수 정의 #####
def send_note(id):
    try:
        id = 'sunsart7'

        #네이버 쪽지 페이지 이동
        driver.get('https://note.naver.com')
        driver.implicitly_wait(3)

        #쪽지 발송창 열기
        driver.find_element_by_xpath('//*[@id="menu_write"]/a[1]').click()

        #쪽지 수신인 삽입
        driver.find_element_by_xpath('//*[@id="who"]').send_keys(id)

        #쪽지 내용 삽입
        content_1 = '쪽지 발송 테스트 \n'
        content_2 = '첫번째줄 \n'
        content_3 = '두번째줄 \n'
        contents = content_1 + content_2 + content_3
        driver.find_element_by_xpath('//*[@id="writeNote"]').send_keys(contents)

        #쪽지 발송
        driver.find_element_by_xpath('//*[@id="cont_fix_area"]/div[6]/div[1]/a[1]').click()

        #쪽지 발송창 닫기
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print('네이버 쪽지 발송완료')
        alert.accept()
    except Exception as e:
        print('네이버 쪽지발송 과정에서 에러발생')
        print(e)
##### 네이버 쪽지 발송 #####


##### 네이버 카페 검색 #####
try:
    #데이터베이스 sqlite3
    conn = sqlite3.connect('naver.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS naver(name text)')

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

            #데이터베이스에서 같은 아이디가 존재하는지 검사
            cursor.execute("SELECT * FROM naver")
            ids = cursor.fetchall()
            if naver_id in ids:
                print('중복됨, 저장안함, 쪽지발송안함')
            else:
                print('중복안됨, 저장함, 쪽지발송함')
                #데이터베이스에 저장
                sql = 'INSERT INTO naver (name) VALUES (?)'
                cursor.execute(sql, (naver_id,))
                conn.commit()
                #쪽지 발송
                send_note(naver_id)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    conn.close()
except Exception as e:
    print('네이버카페 검색과정에서 에러발생')
    print(e)
##### 네이버 카페 검색 #####


