import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))

browser.get('https://www.saucedemo.com')
browser.maximize_window()

user_name = browser.find_element(by=By.ID, value="user-name")
user_name.send_keys('standard_user')

password = browser.find_element(by=By.ID, value='password')
password.send_keys('secret_sauce')

login = browser.find_element(by=By.ID, value='login-button')
login.click()

time.sleep(5)
browser.close()
