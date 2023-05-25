import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# set up base variables
browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
base_url = 'https://www.saucedemo.com'
bad_login = 'locked_out_user'
password_one = 'secret_sauce'

# open new browser window
browser.get(base_url)
browser.maximize_window()

# findelement by id and fill incorrect name
user_name = browser.find_element(by=By.ID, value="user-name")
user_name.send_keys(bad_login)
user_name.send_keys(Keys.BACKSPACE)

# findelement by name and fill password
password = browser.find_element(by=By.NAME, value='password')
password.send_keys(password_one)

# find login button by Xpath and push the button
button_login = browser.find_element(by=By.XPATH, value='//*[@id="login-button"]')
button_login.click()

# check warning input incorrect login/password
warning = browser.find_element(by=By.XPATH, value="//h3[@data-test='error']")
value_warning = warning.text
assert value_warning == 'Epic sadface: Username and password do not match any user in this service'

print('good job')
browser.refresh()

time.sleep(5)
browser.close()
