import time
import names
from random import choice, randrange
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
base_url = 'https://www.saucedemo.com'
login = ['performance_glitch_user', 'standard_user']
multipassword = 'secret_sauce'

# open login page
browser.get(base_url)
browser.maximize_window()

# 1 step: input random username, password and enter
user_name = browser.find_element(by=By.XPATH, value='//*[@id="user-name"]')
user_name.send_keys(choice(login))
password = browser.find_element(by=By.XPATH, value='//*[@id="password"]')
password.send_keys(multipassword)
time.sleep(3)
password.send_keys(Keys.RETURN)
print('1 step: login successful.')

# 2 step: select and add to cart Fleece jacket & Backpack, and remember prices
product_1 = browser.find_element(by=By.XPATH, value='//*[@id="item_5_title_link"]/div')
value_product_1 = product_1.text
price_1 = browser.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_1 = price_1.text
add_cart_1 = browser.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
add_cart_1.click()
product_2 = browser.find_element(by=By.XPATH, value='//*[@id="item_4_title_link"]/div')
value_product_2 = product_2.text
price_2 = browser.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_2 = price_2.text
add_cart_2 = browser.find_element(by=By.XPATH, value='//button[@id="add-to-cart-sauce-labs-backpack"]')
add_cart_2.click()
total_price = float(value_price_1.lstrip('$')) + float(value_price_2.lstrip('$'))
time.sleep(3)
print('2 step: choose products successful\n- product 1: ' + value_product_1 + ', price: ' + value_price_1 + '\n- product 2: ' + value_product_2 + ', price: ' + value_price_2 + '\n-- total price: $' + str(total_price))

# 3 step: go to cart check the products and checkout
cart_icon = browser.find_element(by=By.XPATH, value='//div[@id="shopping_cart_container"]')
cart_icon.click()
cart_product_1 = browser.find_element(by=By.XPATH, value='//*[@id="item_5_title_link"]/div')
value_cart_product_1 = cart_product_1.text
assert value_cart_product_1 == value_product_1
cart_price_1 = browser.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_1 = cart_price_1.text
assert value_price_1 == value_cart_price_1
cart_product_2 = browser.find_element(by=By.XPATH, value='//*[@id="item_4_title_link"]/div')
value_cart_product_2 = cart_product_2.text
assert value_cart_product_2 == value_product_2
cart_price_2 = browser.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_2 = cart_price_2.text
assert value_price_2 == value_cart_price_2
time.sleep(3)
checkout_button = browser.find_element(by=By.XPATH, value='//button[@id="checkout"]')
checkout_button.click()
print('3 step: go to cart successful')

# 4 step: fill the personal information form
first_name = browser.find_element(by=By.XPATH, value='//input[@id="first-name"]')
first_name.send_keys(names.get_first_name())
last_name = browser.find_element(by=By.XPATH, value='//input[@id="last-name"]')
last_name.send_keys(names.get_last_name())
zip_code = browser.find_element(by=By.XPATH, value='//input[@id="postal-code"]')
zip_code.send_keys(randrange(100000, 1000000))
time.sleep(3)
continue_button = browser.find_element(by=By.XPATH, value='//input[@id="continue"]')
continue_button.click()
print('4 step: input personal information successful')

# 5 step: check order overview and finish shopping!
order_product_1 = browser.find_element(by=By.XPATH, value='//*[@id="item_5_title_link"]/div')
value_order_product_1 = order_product_1.text
assert value_order_product_1 == value_cart_product_1
order_price_1 = browser.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_order_price_1 = order_price_1.text
assert value_order_price_1 == value_cart_price_1
order_product_2 = browser.find_element(by=By.XPATH, value='//*[@id="item_4_title_link"]/div')
value_order_product_2 = order_product_2.text
assert value_order_product_2 == value_cart_product_2
order_price_2 = browser.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_order_price_2 = order_price_2.text
assert value_order_price_2 == value_cart_price_2
order_total_price = browser.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_order_total_price = order_total_price.text
item_total = float(value_order_total_price[13:])
assert item_total == total_price
time.sleep(3)
checkout_button = browser.find_element(by=By.XPATH, value='//button[@id="finish"]')
checkout_button.click()
print('5 step: checkout successful, finish!')

browser.close()