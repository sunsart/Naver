from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#일정 이벤트 발생시까지 대기하는 코드
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#네이버 쪽지 발송
def send_note(naver_id):
    try:
        #네이버 쪽지 페이지 이동
        driver = webdriver.Chrome()
        driver.get('https://note.naver.com')
        driver.implicitly_wait(3)

        #쪽지 발송창 열기
        driver.find_element_by_xpath('//*[@id="menu_write"]/a[1]').click()

        #쪽지 수신인 삽입
        driver.find_element_by_xpath('//*[@id="who"]').send_keys(naver_id)

        #쪽지 내용 삽입
        content = '쪽지 발송 테스트'
        driver.find_element_by_xpath('//*[@id="writeNote"]').send_keys(content)

        #쪽지 발송
        driver.find_element_by_xpath('//*[@id="cont_fix_area"]/div[6]/div[1]/a[1]').click()

        #쪽지 발송창 닫기
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        #print(alert.text)
        alert.accept()
    except Exception as e:
        print('네이버 쪽지발송 과정에서 에러발생')
        print(e)