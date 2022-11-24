from selenium.webdriver.common.by import By
from pages.base_page import Basepage


class home_page(Basepage):
    ADD_REMOVE_ELEMENTS = (By.LINK_TEXT, f'Add/Remove Elements')
    DROPDOWN = (By.LINK_TEXT, f'Dropdown')
    FORM_AUTH = (By.LINK_TEXT, 'Form Authentication')
    FORGOT_PASS = (By.LINK_TEXT, f'Forgot Password')
    HOME_PAGE = 'https://the-internet.herokuapp.com/'

    def navigate_to_page1(self):
        self.chrome.get(*self.HOME_PAGE)
        self.chrome.find_element(*self.ADD_REMOVE_ELEMENTS).click()

    def navigate_to_page2(self):
        self.chrome.get(*self.HOME_PAGE)
        self.chrome.find_element(*self.DROPDOWN).click()

    def navigate_to_page3(self):
        self.chrome.get(*self.HOME_PAGE)
        self.chrome.find_element(*self.FORM_AUTH).click()

    def navigate_to_page4(self):
        self.chrome.get(*self.HOME_PAGE)
        self.chrome.find_element(*self.FORGOT_PASS).click()
