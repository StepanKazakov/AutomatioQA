import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class ClientPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    zipcode = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_zipcode(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.zipcode)))
    def get_continue_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Actions
    def input_first_name(self):
        self.get_first_name().send_keys('Max')
        print('input name')
        time.sleep(1)

    def input_last_name(self):
        self.get_last_name().send_keys('GOF')
        print('input last name')
        time.sleep(1)

    def input_zipcode(self):
        self.get_zipcode().send_keys('1234')
        print('input zipcode')
        time.sleep(1)

    def click_continue_button(self):
        self.get_continue_button().click()
        print('click continue button')
        time.sleep(1)

    # Methods
    def input_client_data(self):
        self.get_current_url()
        self.input_first_name()
        self.input_last_name()
        self.input_zipcode()
        self.click_continue_button()
