import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class MainPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'
    menu = '//button[@id="react-burger-menu-btn"]'
    about = '//a[@id="about_sidebar_link"]'
    logout = '//a[@id="logout_sidebar_link"]'

    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_about_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.about)))

    # Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('select and add backpack into cart')
        time.sleep(1)

    def click_cart_button(self):
        self.get_cart_button().click()
        print('go to cart')

    def click_menu_button(self):
        self.get_menu_button().click()
        print('open menu')

    def click_about_button(self):
        self.get_about_button().click()
        print('open about')

    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart_button()

    def open_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.assert_url(result='https://saucelabs.com')
