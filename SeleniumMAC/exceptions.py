import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

base_url = 'https://demoqa.com/dynamic-properties'
browser = webdriver.Firefox()
browser.get(base_url)
# browser.maximize_window()

# явные ожидания устанавливаются индивидуально для каждого элемента и срабатывают только когда элемент станет доступным для действия
visible_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable("//button[@id='visibleAfter']"))
visible_button.click()
print('ok')

# неявные ожидания будут срабатывать для каждой операции теста и ждать до 10 секунд появления элементов в DOM
# browser.implicitly_wait(10)
# visible_button = browser.find_element(By.XPATH, value="//button[@id='visibleAfter']")
# visible_button.click()
# print('ok')

# обработка исключений
# try:
#     visible_button = browser.find_element(By.XPATH, value="//button[@id='visibleAfter']")
#     visible_button.click()
#
# except NoSuchElementException as exception:
#     print('NoSuchElementException')
#     browser.refresh()
#     time.sleep(6)
#     visible_button = browser.find_element(By.XPATH, value="//button[@id='visibleAfter']")
#     visible_button.click()
#     print('Click visible button')

browser.close()