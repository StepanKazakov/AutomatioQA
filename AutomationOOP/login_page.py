import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NewLogin():

    def __init__(self, browser):
        self.browser = browser


    def authorisation(self, login_name, login_pass):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((
                                               By.XPATH, '//*[@id="user-name"]'))) \
                                       .send_keys(login_name)
        time.sleep(2)

        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((
                                               By.XPATH, '//*[@id="password"]'))) \
                                       .send_keys(login_pass, Keys.RETURN)