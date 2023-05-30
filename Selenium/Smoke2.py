import time
import names
from random import randrange
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
base_url = 'https://www.saucedemo.com'
login = 'standard_user'
multipassword = 'secret_sauce'

# set up all products XPATHs to dictionaries
products_names = {1: 'Sauce Labs Backpack', 2: 'Sauce Labs Bike Light', 3: 'Sauce Labs Bolt T-Shirt',
                  4: 'Sauce Labs Fleece Jacket', 5: 'Sauce Labs Onesie', 6: 'Test.allTheThings() T-Shirt (Red)'}
products_xpath = {1: '//*[@id="item_4_title_link"]/div', 2: '//*[@id="item_0_title_link"]/div',
                  3: '//*[@id="item_1_title_link"]/div', 4: '//*[@id="item_5_title_link"]/div',
                  5: '//*[@id="item_2_title_link"]/div', 6: '//*[@id="item_3_title_link"]/div'}
products_prices = {1: '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div',
                   2: '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div',
                   3: '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div',
                   4: '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div',
                   5: '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div',
                   6: '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div'}
add_to_cart_btns = {1: '//*[@id="add-to-cart-sauce-labs-backpack"]',
                   2: '//*[@id="add-to-cart-sauce-labs-bike-light"]',
                   3: '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]',
                   4: '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]',
                   5: '//*[@id="add-to-cart-sauce-labs-onesie"]',
                   6: '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'}

# preliminary steps for obtaining the correct product number
print("Приветствуем Вас в нашем интернет-магазине!")

def check_number(x):
    try:
        while x not in (1, 2, 3, 4, 5, 6):
            x = int(input('Введено недопустимое значение, укажите цифру от 1 до 6\n'))
        return x
    except (ValueError, KeyError, NameError):
        print('Какая неудача, вы нажали не ту кнопку!')

try:
    product_number = check_number(int(input(
        'Выберите один из следующих товаров и укажите его номер:\n1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light\n3 - '
        'Sauce Labs Bolt T-Shirt\n4 - Sauce Labs Fleece Jacket\n5 - Sauce Labs Onesie\n6 - Test.allTheThings() T-Shirt (Red)\n')))
except (ValueError, KeyError, NameError):
    print('Какая жалость, вы нажали не ту кнопку!')

try:
    print('Прекрасный выбор! Вы выбрали: ' + products_names[product_number] + '\nБерите два, не пожалеете!')
except (ValueError, KeyError, NameError):
    print('Попробуйте в другой раз')

# 1 step: open site and login into market
browser.get(base_url)
browser.maximize_window()
user_name = browser.find_element(by=By.XPATH, value='//*[@id="user-name"]')
user_name.send_keys(login)
password = browser.find_element(by=By.XPATH, value='//*[@id="password"]')
password.send_keys(multipassword)
time.sleep(3)
password.send_keys(Keys.RETURN)
print('1 step: login successful.')

# 2 step: add to cart selected product and remember price
product = browser.find_element(by=By.XPATH, value=products_xpath[product_number])
value_product = product.text
price = browser.find_element(by=By.XPATH, value=products_prices[product_number])
value_price = price.text
add_cart = browser.find_element(by=By.XPATH, value=add_to_cart_btns[product_number])
add_cart.click()
assert products_names[product_number] == value_product
time.sleep(3)
print('2 step: add to card product successful\n- product: ' + value_product + ', price: ' + value_price)

# 3 step: go to cart check the product and checkout
cart_icon = browser.find_element(by=By.XPATH, value='//div[@id="shopping_cart_container"]')
cart_icon.click()
cart_product = browser.find_element(by=By.XPATH, value=products_xpath[product_number])
value_cart_product = cart_product.text
assert value_cart_product == value_product
cart_price = browser.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price = cart_price.text
assert value_price == value_cart_price
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
order_product = browser.find_element(by=By.XPATH, value=products_xpath[product_number])
value_order_product = order_product.text
assert value_order_product == value_cart_product
order_price = browser.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_order_price = order_price.text
assert value_order_price == value_cart_price
time.sleep(3)
checkout_button = browser.find_element(by=By.XPATH, value='//button[@id="finish"]')
checkout_button.click()
print('5 step: checkout successful, finish!')

browser.close()