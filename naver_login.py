from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pyperclip

#네이버 로그인
def login(id, pw):
    try:
        driver = webdriver.Chrome()
        driver.get('https://nid.naver.com/nidlogin.login')
        time.sleep(2)

        pyperclip.copy(id)
        driver.find_element_by_name('id').send_keys(Keys.CONTROL, 'v')
        time.sleep(np.random.rand())    #기계적인 입력에 의한 캡챠를 피하기 위해 랜덤시간만큼 간격을 줌

        pyperclip.copy(pw)
        driver.find_element_by_name('pw').send_keys(Keys.CONTROL, 'v')
        time.sleep(np.random.rand())    #기계적인 입력에 의한 캡챠를 피하기 위해 랜덤시간만큼 간격을 줌

        driver.find_element_by_id('log.login').click() 
        time.sleep(2)
        print('네이버 로그인 성공')

    except Exception as e:
        print('네이버 로그인 과정에서 에러발생')
        print(e)

