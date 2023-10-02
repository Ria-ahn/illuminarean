from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
import time



options = Options()

options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)


url ='https://illuminarean.com/'
driver.get(url)

# 옵선박스 선택
def choose ( name , choo_name):
    driver.find_element(By.ID, name).click()
    option = driver.find_element(By.XPATH, '//*[text()="'+ choo_name +'"]')
    driver.execute_script('arguments[0].scrollIntoView();', option)
    option.click()



# 모달 창 제거
x_btn = 'body > div.ReactModalPortal > div > div > div > div > button.css-1lby940.e1iwydzj0 > svg'
driver.find_element(By.CSS_SELECTOR,x_btn).click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[contains(text(),"Work")]').click()
driver.find_element(By.XPATH, '//*[contains(text(),"GOODVIBE WORKS 바로가기")]').click()

# 새창으로 전환
# print(driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])



time.sleep(5)
driver.find_element(By.XPATH, '//*[contains(text(),"무료 체험 신청")]').click()

driver.find_element(By.ID,'companyName').send_keys('QA신입사원')
driver.find_element(By.ID,'ceoName').send_keys('안혜선')


driver.find_element(By.ID,'businessType').click()
option = driver.find_element(By.XPATH, '//*[text()="개인"]')
driver.execute_script('arguments[0].scrollIntoView();', option)
option.click()


# 드롭다운 선택을 함수로 생성하여 처리
choose( 'businessType' , "개인" )
choose( 'scale' , "21-50 명" )

driver.find_element(By.ID,'name').send_keys('안혜선')
driver.find_element(By.ID,'email').send_keys('ahn@test.kr')
driver.find_element(By.ID,'mobile').send_keys('010-1234-5678')



# 담당업무 부분 처리

input_box =    '/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/button/p/div/input'
cal_image = '/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[1]/button[1]'
style_image = '/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[1]/button[6]'
registration = '/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[2]/button[2]'

# 입력으로 옵션 선택하기 (회계) 
driver.find_element(By.CLASS_NAME,'duties').click()
driver.find_element(By.XPATH,input_box).send_keys('회계')
driver.find_element(By.XPATH,cal_image).click()
driver.find_element(By.XPATH,registration).click()

# 하단 이미지로 선택하기(스타일리스트) 
driver.find_element(By.CLASS_NAME,'duties').click()
driver.find_element(By.XPATH,style_image).click()
driver.find_element(By.XPATH,registration).click()

# 신청취소 버튼
driver.find_element(By.XPATH, '/html/body/div[6]/button').click()