import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
browser = webdriver.Firefox()
browser.get(base_url)
browser.maximize_window()

action = ActionChains(browser)

price = browser.find_element(By.XPATH, '//input[@id="id1"]')
action.click_and_hold(price).move_by_offset(120, 0).release().perform()
time.sleep(3)

browser.close()
