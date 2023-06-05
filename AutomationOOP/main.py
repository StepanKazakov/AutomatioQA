from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

import login_page


class TestLogin():

    def test_select_product(self):
        browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
        base_url = 'https://www.saucedemo.com'
        login_user = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        multipassword = 'secret_sauce'

        browser.get(base_url)
        browser.maximize_window()
        print('Start test')

        login = login_page.NewLogin(browser)
        login.authorisation(login_user[0], multipassword)
        print('Standard user login success')

        login.authorisation(login_user[1], multipassword)
        print('Locked user locked out')

        login.authorisation(login_user[2], multipassword)
        print('Problem user login success')

        login.authorisation(login_user[3], multipassword)
        print('Glitch user login success')


test = TestLogin()
test.test_select_product()
