import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from main_project.base.base_class import Base


class Finish(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Methods
    def screenshot(self):
        self.get_current_url()
        self.assert_url(result='https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
