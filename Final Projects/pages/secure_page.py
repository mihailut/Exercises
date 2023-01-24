from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import Basepage


class Sign_In_Page(Basepage):
    USER_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOGOUT_BUTTON = (By.LINK_TEXT, f"Logout")

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()

    def set_email(self, email):
        self.chrome.find_element(*self.USER_INPUT).send_keys(email)

    def set_pwd(self, pwd):
        self.chrome.find_element(*self.PASS_INPUT).send_keys(pwd)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def successful_login(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual_url, expected_url, "The URL doesn't match")

    def element_visible(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, f'//*[@id="flash"]'),
                                                      "You logged into a secure area!" or "Your username is invalid!"))
        if actual:
            print('Message found is correct')
        else:
            print(f'Message found incorrect')
        self.assertTrue(actual.is_displayed(), 'The message is displayed.')

    def logout(self):
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual_url, expected_url, "The URL doesn't match")
