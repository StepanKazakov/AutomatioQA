import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class CartPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    checkout_button = '//button[@id="checkout"]'

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('click checkout button')
        time.sleep(1)

    # Methods
    def checkout(self):
        self.get_current_url()
        self.click_checkout_button()
