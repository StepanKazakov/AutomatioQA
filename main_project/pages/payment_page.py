import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class PaymentPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    finish_button = '//button[@id="finish"]'

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))


    # Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print('click finish button')
        time.sleep(1)

    # Methods
    def payment(self):
        self.get_current_url()
        self.click_finish_button()
