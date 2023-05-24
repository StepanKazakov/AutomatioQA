import time
from selenium import webdriver
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

# findelement by name and fill password
password = browser.find_element(by=By.NAME, value='password')
password.send_keys(password_one)

# find login button by Xpath and push the button
button_login = browser.find_element(by=By.XPATH, value='//*[@id="login-button"]')
button_login.click()

# check web page by title text
text_products = browser.find_element(by=By.XPATH, value='//span[@class="title"]')
value_text_products = text_products.text
assert value_text_products == 'Products'

# check correct url
url = 'https://www.saucedemo.com/inventory.html'
get_url = browser.current_url
assert url == get_url
print('super')

time.sleep(5)
browser.close()
