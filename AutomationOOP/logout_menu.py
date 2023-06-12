import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Logout():

    def __init__(self, browser):
        self.browser = browser

    def select_menu_logout(self):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((
                                               By.XPATH, '//button[@id="react-burger-menu-btn"]'))) \
                                       .click()
        time.sleep(2)

        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((
                                               By.XPATH, '//a[@id="logout_sidebar_link"]'))) \
                                       .click()