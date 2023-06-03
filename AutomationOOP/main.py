import time
import login_page
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_1():

    def test_select_product(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
        base_url = 'https://www.saucedemo.com'
        browser.get(base_url)
        browser.maximize_window()

        print('Start test')

        login_performance = 'performance_glitch_user'
        multipassword = 'secret_sauce'

        login = login_page.new_login(browser)
        login.authorisation(login_performance, multipassword)

        print('The end')


test = Test_1()
test.test_select_product()
