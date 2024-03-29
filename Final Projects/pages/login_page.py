from selenium.webdriver.common.by import By
from pages.base_page import Basepage


class Sign_In_Page(Basepage):
    USER_INPUT = (By.XPATH, f'//input[@id="username"]')
    PASS_INPUT = (By.XPATH, f'//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()

    def set_email(self, email):
        self.chrome.find_element(*self.USER_INPUT).send_keys(email)

    def set_pwd(self, pwd):
        self.chrome.find_element(*self.PASS_INPUT).send_keys(pwd)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual_url, expected_url, "The URL doesn't match")
