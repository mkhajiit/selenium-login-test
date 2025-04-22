import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin(unittest.TestCase):
    # 테스트 실행 전 실행되는 코드
    def setUp(self):
        options = webdriver.ChromeOptions()  # 설정객체
        options.add_argument("--start-maximized")  # 브라우저 창을 최대화로 열도록 설정
        options.add_argument("--headless")  # headless 모드로 실행

        # 드라이버 설정
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=options
        )

        self.driver.get("http://localhost:5173/")  # 테스트할 사이트로 이동
# https://selenium-login-test.vercel.app/
    # 테스트 실행 후 무조건 실행되는 코드
    def tearDown(self):
        time.sleep(2)  # 프로그램을 2초 동안 멈추는 코드
        self.driver.quit()  # 브라우저 종료

    # 실제 테스트 메서드
    def test_login_failure(self):
        driver = self.driver

        id = "테스터"
        pwd = "123456"  # 실패하는 비밀번호

        # 아이디, 비밀번호 입력란 찾기
        id_input = driver.find_element(By.CLASS_NAME, "id-input")
        pwd_input = driver.find_element(By.CLASS_NAME, "pwd-input")

        id_input.send_keys(id)
        pwd_input.send_keys(pwd)

        # 로그인 버튼 클릭
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()

        # alert이 뜰 때까지 최대 5초 대기
        WebDriverWait(driver, 5).until(EC.alert_is_present())

        # alert 객체 가져오기
        alert = Alert(driver)

        # 조건이 False이면 AssertionError를 발생시키고, 뒤에 있는 메시지를 같이 출력
        self.assertEqual(
            alert.text,
            '로그인이 성공했습니다.',
            f"로그인 실패! 실제 메시지: {alert.text}, 입력된 아이디: {id}, 입력된 비밀번호: {pwd}"
        )

        # alert 확인창 누르기
        alert.accept()

if __name__ == "__main__":
    unittest.main()