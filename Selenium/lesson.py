import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
base_url = 'https://www.saucedemo.com'
login = 'standard_user'
password_one = 'secret_sauce'


browser.get(base_url)
browser.maximize_window()

# findelement by id and fill name
user_name = browser.find_element(by=By.ID, value="user-name")
user_name.send_keys(login)
#user_name.clear()

# findelement by name and fill password
password = browser.find_element(by=By.NAME, value='password')
password.send_keys(password_one)
time.sleep(3)
#browser.refresh()

# find login button by Xpath and push the button
button_login = browser.find_element(by=By.XPATH, value='//*[@id="login-button"]')
button_login.click()
time.sleep(3)
browser.back()
time.sleep(3)
browser.forward()
# # check web page by title text
# text_products = browser.find_element(by=By.XPATH, value='//span[@class="title"]')
# value_text_products = text_products.text
# assert value_text_products == 'Products'
#
# # check correct url
# url = 'https://www.saucedemo.com/inventory.html'
# get_url = browser.current_url
# assert url == get_url
# print('super')
#
# # click keyboard buttons
# filter = browser.find_element(by=By.XPATH, value='//select[@data-test="product_sort_container"]')
# filter.click()
# time.sleep(2)
# filter.send_keys(Keys.DOWN)
# filter.send_keys(Keys.RETURN)

# scroll screen
# browser.execute_script('window.scrollTo(0, 500)')
# action = ActionChains(browser)
# linkedin = browser.find_element(By.XPATH, '//footer/ul/li[3]/a')
# time.sleep(2)
# action.move_to_element(linkedin).perform()
# time.sleep(3)

# # take screenshot and put into folder
# sys_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M')
# name_screen = 'screen' + sys_date + '.png'
# browser.save_screenshot('C:/Users/user/PycharmProjects/AutomatioQA/Selenium/screens/' + name_screen)
#
# menu = browser.find_element(By.ID, value='react-burger-menu-btn')
# menu.click()
time.sleep(3)
browser.close()
