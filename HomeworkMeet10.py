import unittest
import HtmlTestRunner
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Homeworks.homework_done_by_me.HomeworkMeet9 import Test
# for Ex. 1
from From_Classes.Meet10.test_alerts import Alerts
from From_Classes.Meet10.test_keys import Keyboard
from From_Classes.Meet10.test_context_menu import ContextMenu
from From_Classes.Meet10.test_auth import Authentication
from From_Classes.Meet10.test_browser import Browser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screenshot import Screenshot
from selenium.webdriver.common.keys import Keys
import os
from pathlib import Path


# Ex. 1

class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Result Name of Tests from 16.11.2022'
        )

        runner.run(tests_to_run)


# Ex. 2


class testing_browser(unittest.TestCase):
    PAGE = (By.LINK_TEXT, 'Basic Auth')
    USERNAME = 'admin'
    PASSWORD = 'admin'
    BUTTON_ADD = (By.XPATH, '//button[text()="Add Element"]')
    BUTTON_DEL = (By.XPATH, '//button[text()="Delete"]')

    def setUp(self) -> None:
        s = Service(GeckoDriverManager().install())
        self.firefox = webdriver.Firefox(service=s)
        self.firefox.maximize_window()
        self.firefox.get('https://the-internet.herokuapp.com/')
        self.firefox.implicitly_wait(1)

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_log(self):
        self.firefox.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        sleep(2)
        actual = WebDriverWait(self.firefox, 2).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div['
                                                                                                  '2]/div/div/p'),
                                                                                       "Congratulations! You must "
                                                                                       "have the proper credentials."))
        if actual:
            print('The displayed message is correct.')
        else:
            print('The displayed message is not correct.')

    def test_element(self):
        self.firefox.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        sleep(1)
        self.firefox.find_element(*self.BUTTON_ADD).click()
        sleep(1)
        self.firefox.find_element(*self.BUTTON_ADD).click()
        sleep(1)
        self.firefox.find_element(*self.BUTTON_ADD).click()
        sleep(1)
        self.firefox.find_element(*self.BUTTON_ADD).click()
        sleep(1)
        self.firefox.find_element(*self.BUTTON_DEL).click()
        sleep(1)
        self.firefox.find_element(*self.BUTTON_DEL).click()
        sleep(1)
        ob = Screenshot.Screenshot()
        ob.full_Screenshot(self.firefox, save_path=r'C:\Users\Mihail\Desktop\IT FACTORY\screenshots',
                           image_name='Myimage.png')
        sleep(1)

    def test_disappear(self):
        self.firefox.find_element(By.LINK_TEXT, 'Disappearing Elements').click()
        self.firefox.find_element(By.LINK_TEXT, 'About').click()
        sleep(1)
        actual = WebDriverWait(self.firefox, 2).until(
            EC.text_to_be_present_in_element((By.XPATH, '/html/body/h1'), "Not Found"))
        if actual:
            print('The elements on this page is disappeard.')
        else:
            print('The elements on this page is visible.')
        sleep(1)
        self.firefox.back()
        sleep(1)
        self.firefox.find_element(By.LINK_TEXT, 'Contact Us').click()
        actual = WebDriverWait(self.firefox, 2).until(
            EC.text_to_be_present_in_element((By.XPATH, '/html/body/h1'), "Not Found"))
        if actual:
            print('The elements on this page is disappeard.')
        else:
            print('The elements on this page is visible.')
        sleep(1)
        self.firefox.back()
        sleep(1)
        self.firefox.find_element(By.LINK_TEXT, 'Portfolio').click()
        actual = WebDriverWait(self.firefox, 2).until(
            EC.text_to_be_present_in_element((By.XPATH, '/html/body/h1'), "Not Found"))
        if actual:
            print('The elements on this page is disappeard.')
        else:
            print('The elements on this page is visible.')
        sleep(1)
        self.firefox.back()

    def test_files(self):
        self.firefox.find_element(By.LINK_TEXT, 'File Download').click()
        self.firefox.find_element(By.LINK_TEXT, 'selenium.png').click()
        if os.path.exists(r"C:\Users\Mihail\Downloads\selenium.png"):
            print('The file has been downloaded.')
        else:
            print('The file was not downloaded.')
        self.firefox.find_element(By.LINK_TEXT, 'white.jpg').click()
        if os.path.exists(r"C:\Users\Mihail\Downloads\white.jpg"):
            print('The file has been downloaded.')
        else:
            print('The file was not downloaded.')
        self.firefox.find_element(By.LINK_TEXT, 'Honey Resume.pdf').click()
        if os.path.exists(r"C:\Users\Mihail\Downloads\Honey Resume.pdf"):
            print('The file has been downloaded.')
        else:
            print('The file was not downloaded.')
        if os.path.exists(r"C:\Users\Mihail\Downloads\test.csv"):
            print('The file has been downloaded.')
        else:
            print('The file was not downloaded.')
        sleep(2)