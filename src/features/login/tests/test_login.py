from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() # 설정객체
options.add_argument("--start-maximized") # 브라우저 창을 최대화로 열도록 설정

# 드라이버 설정
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=options
)

try:
  driver.get("http://localhost:5173/")

  id_input = driver.find_element(By.CLASS_NAME, "id-input")
  pwd_input = driver.find_element(By.CLASS_NAME, "pwd-input")

  id_input.send_keys("테스터2")
  pwd_input.send_keys("1234")

  login_button = driver.find_element(By.TAG_NAME, "button")
  login_button.click()

  WebDriverWait(driver, 5).until(EC.alert_is_present())
  # alert 객체 가져오기
  alert  = Alert(driver)
  
  assert alert.text == '로그인이 성공했습니다.'

  print("검증이 성공했습니다.")

  # alert 확인창 누르기
  alert.accept()

finally:
  time.sleep(2) # 프로그램을 2초 동안 멈추는 코드
  driver.quit()