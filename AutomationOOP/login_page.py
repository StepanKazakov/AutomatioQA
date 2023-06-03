import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class new_login():
    def __init__(self, browser):
        self.browser = browser

    def authorisation(self, login_name, login_pass):

        user_name = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys(login_name)

        password = WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password.send_keys(login_pass)
        password.send_keys(Keys.RETURN)
