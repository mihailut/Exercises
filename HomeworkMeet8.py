from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Screenshot import Screenshot
from selenium.webdriver.support.select import Select
s = Service(ChromeDriverManager().install())

# selector by link text
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'A/B Testing').click()
# sleep(2)
# chrome.quit()
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
# sleep(2)
# chrome.quit()
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Redirect Link').click()
# sleep(2)
# chrome.quit()
#
# # selector by partial link text
# # 1
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Upload').click()
# sleep(2)
# chrome.quit()
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'WYSIWYG').click()
# sleep(2)
# chrome.quit()
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Basic').click()
# sleep(2)
# chrome.quit()

# selector by id
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.ID, 'search_query_top').send_keys('dress')
# sleep(2)
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.ID, 'contact-link').click()
# sleep(2)
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php?controller=contact')
# chrome.find_element(By.ID, 'email').send_keys('alinbambus@yahoo.com')
# sleep(2)
# chrome.quit()

# selector by name
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php/')
# chrome.find_element(By.NAME, 'search_query').send_keys('shoes')
# # 2
# chrome.find_element(By.NAME, 'submit_search').click()
# sleep(2)
# chrome.quit()
# 3
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php/')
# chrome.find_element(By.NAME, 'email').send_keys('elonmusk30@gmail.com')
# sleep(2)
# chrome.quit()

# selector by Tag

# 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_elements(By.TAG_NAME, 'input')
# # 2
# chrome.find_elements(By.TAG_NAME, 'input')[0].send_keys('Google')
# # 3
# chrome.find_elements(By.TAG_NAME, 'input')[1].send_keys('Prahova')
# input_list = chrome.find_elements(By.TAG_NAME, 'input')[2]
# input_list.send_keys('Kogalniceanu')
# ob = Screenshot.Screenshot()
# img_url = ob.full_Screenshot(chrome, save_path=r'C:\Users\Mihail\Desktop\IT FACTORY\screenshots',
#                              image_name='Myimage.png')
# sleep(2)
# chrome.quit()

# selector by class name
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php')
#
# list1 = chrome.find_elements(By.CLASS_NAME, 'login')
# list1[0].click()
# sleep(2)
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_elements(By.CLASS_NAME, 'product_img_link')[3].click()
# sleep(2)
# # 3
# chrome.find_element(By.CLASS_NAME, 'sf-with-ul').click()
# sleep(2)
# chrome.quit()

# selector by CSS
# 1 attribute value
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter address"').send_keys('Istanbul')
# sleep(2)
# 2 id
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input#street_number').send_keys('244A')
# sleep(2)
# 3 class
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('33')
# sleep(2)
# chrome.quit()

"""selector by XPATH"""


# attribute value
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys('Macarena')
# # 2
# chrome.find_element(By.XPATH, '//input[@id="street_number"]').send_keys('99999')
# # 3
# chrome.find_element(By.XPATH, '//input[@id="locality"]').send_keys('Cluj-Napoca')
# screenshot1 = Screenshot.Screenshot()
# img_url = screenshot1.full_Screenshot(chrome, save_path=r'C:\Users\Mihail\Desktop\IT FACTORY\screenshots',
#                                       image_name='Myimage2.png')
# sleep(2)
# chrome.quit()

# text on the element
# # 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/buttons')
# chrome.find_element(By.XPATH, '//button[text()="Primary"]').click()
# sleep(2)
# # 2
# chrome.get('https://formy-project.herokuapp.com')
# chrome.find_element(By.XPATH, '//a[text()="Form"]').click()
# sleep(2)
# # 3
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//a[text()="Formy"]').click()
# sleep(2)
# chrome.quit()

# or using PIPE

# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/form')
# x = chrome.find_element(By.XPATH, '//input[@id="last-name"] | input[@id="first-name"]')
# x.send_keys('Jhonny')
# x.clear()
# x.send_keys('Deep')
# sleep(2)
# chrome.quit()

# with *

# chrome = webdriver.Chrome(service=s)
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.XPATH, '//a[text()="Form Authentication"]').click()
# chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys('mynameisjhon@yahoo.com')
# sleep(2)
# chrome.quit()

# index of list

# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# list2 = chrome.find_elements(By.XPATH, '//input[@class="is_required validate account_input form-control"]')
# list2[2].send_keys('Password')
# sleep(2)
# chrome.quit()

# parent

# chrome = webdriver.Chrome(service=s)
# chrome.get('https://the-internet.herokuapp.com')
# chrome.find_element(By.XPATH, '//a[text()="Form Authentication"]').click()
# chrome.find_element(By.XPATH, '//parent::div//input[@id="username"]').send_keys('Mariciu')
# sleep(2)
# chrome.quit()

# previous brother

# chrome = webdriver.Chrome(service=s)
# chrome.get('https://the-internet.herokuapp.com')
# chrome.find_element(By.XPATH,
#                     '//a[text()="Form Authentication"]').click()
# chrome.find_element(By.XPATH,
#                     '//parent::div//preceding-sibling::form//input[@name="password"]').send_keys('Password99')
# sleep(2)
# chrome.quit()

# function
# class choose:
#     element = None
#
#
# def choose_element(parameter):
#     chrome = webdriver.Chrome(service=s)
#     chrome.get('https://formy-project.herokuapp.com/autocomplete')
#     x = chrome.find_element(By.XPATH, parameter)
#     x.send_keys('Turkey')
#     sleep(2)
#     chrome.quit()
#
#
# choose_element('//input[@id="locality"]')
