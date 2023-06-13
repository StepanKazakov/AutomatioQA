import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class NewLogin(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators & variables
    url = 'https://www.saucedemo.com'
    user_name = '//*[@id="user-name"]'
    password = '//*[@id="password"]'
    title_products = '//span[@class="title"]'

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_title_products(self):
        return WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located((By.XPATH, self.title_products)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('input user name')
        time.sleep(1)

    def input_password(self, password):
        self.get_password().send_keys(password, Keys.RETURN)
        print('input password')

    # Methods
    def authorisation(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.get_current_url()
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.assert_word(self.get_title_products(), 'Products')
