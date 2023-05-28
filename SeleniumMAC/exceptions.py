import time
from datetime import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

base_url = 'https://demoqa.com/dynamic-properties'
browser = webdriver.Firefox()
browser.get(base_url)
browser.maximize_window()

try:
    visible_button = browser.find_element(By.XPATH, value="//button[@id='visibleAfter']")
    visible_button.click()

except NoSuchElementException as exception:
    print('NoSuchElementException')
    browser.refresh()
    time.sleep(6)
    visible_button = browser.find_element(By.XPATH, value="//button[@id='visibleAfter']")
    visible_button.click()
    print('Click visible button')

browser.close()