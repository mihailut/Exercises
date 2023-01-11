import unittest
from time import sleep
from unittest import TestCase

import selenium.webdriver.support.color
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(TestCase):
    # LOGIN_BTN = (By.LINK_TEXT, 'Form Authentication')
    # PAGE_TITLE = (By.LINK_TEXT, 'The Internet')
    # MESSAGE_ERROR_LOGIN = (By.XPATH, '//div//div//div[@class="flash error"]')
    # MESSAGE_SUCCESS_LOGIN = (By.XPATH, '//div//div//div[@class="flash success"]')
    SIGN_UP_BUTTON = (By.LINK_TEXT, 'Sign up.')
    PERSON_BUTTON = (By.CSS_SELECTOR, 'input[value="personal"]')
    CONTINUE_BUTTON1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]')
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    CONTINUE_BUTTON2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    CONTINUE_BUTTON3 = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    MESSAGE = (By.XPATH, "f'//*[@id='root']/div/div[4]/div[2]/div/div[2]/div/p")
    MESSAGE_EMAIL_INPUT = (By.XPATH, f'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(1)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_navigate_to_sign_up_page(self):
        self.chrome.get("https://jules.app/sign-in")
        self.chrome.find_element(*self.SIGN_UP_BUTTON).click()
        sleep(1)
        self.chrome.find_element(*self.PERSON_BUTTON).click()
        sleep(1)
        self.chrome.find_element(*self.CONTINUE_BUTTON1).click()
        sleep(1)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys('firstname')
        sleep(1)
        self.chrome.find_element(*self.CONTINUE_BUTTON2).click()
        sleep(1)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys('lastname')
        sleep(1)
        self.chrome.find_element(*self.CONTINUE_BUTTON3).click()
        sleep(1)
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys('email')
        # sleep(1)
        # self.chrome.find_element(*self.EMAIL_INPUT).send_keys(Keys.CONTROL + 'a')
        # self.chrome.find_element(*self.EMAIL_INPUT).send_keys(Keys.BACKSPACE)
        # self.chrome.find_element(*self.EMAIL_INPUT).send_keys('email@email.com')
        sleep(1)
        element = self.chrome.find_element(*self.MESSAGE_EMAIL_INPUT)
        print(element.is_displayed())
        sleep(2)
    # def click_sign_up_button(self):
    #     self.chrome.find_element(*self.SIGN_UP_BUTTON).click()
    #
    # def select_person(self):
    #     self.chrome.find_element(*self.PERSON_BUTTON).click()
    #
    # def click_continue_button1(self):
    #     self.chrome.find_element(*self.CONTINUE_BUTTON1).click()
    #
    # def set_first_name(self, first_name):
    #     self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
    #
    # def click_continue_button2(self):
    #     self.chrome.find_element(*self.CONTINUE_BUTTON2).click()
    #
    # def set_last_name(self, last_name):
    #     self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
    #
    # def click_continue_button3(self):
    #     self.chrome.find_element(*self.CONTINUE_BUTTON3).click()
    #
    # def set_email(self, email):
    #     self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)
    #
    # def verify_display_invalid_email(self):
    #     actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
    #                                                  ((By.XPATH, f'//div/p'),
    #                                                   "Please enter a valid email address."))
    #     if actual:
    #         print('Message found is correct')
    #     else:
    #         print(f'Message found incorrect')
    #     self.assertTrue(actual.is_displayed(), 'The message is displayed.')
