import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import login_page, logout_menu


class TestLogin():
    browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
    browser.get('https://www.saucedemo.com')
    browser.maximize_window()
    print('Start test')

    def users_login(self, browser):
        # set up users variables
        login_user = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        multipassword = 'secret_sauce'

        # testing all users start in cycle
        for i in range(len(login_user)):
            # go to login_page module
            login_page.NewLogin(browser).authorisation(login_user[i], multipassword)
            try:
            # check result web page after login by title text
                title_products = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located((
                                                                        By.XPATH, '//span[@class="title"]')))
                value_title = title_products.text
                assert value_title == 'Products'
            # if the login was successful print 'success' and logout current user
                print(login_user[i] + ' login success')
            # go to logout_menu module
                logout_menu.Logout(browser).select_menu_logout()
                print(login_user[i] + ' logout success')
                time.sleep(2)
            # clean inputs after previous user
                browser.refresh()
            except TimeoutException:
            # if the login was unsuccessful print 'cannot login' and clean inputs
                print(login_user[i] + ' cannot login')
                browser.refresh()
                time.sleep(2)


TestLogin().users_login(browser=TestLogin.browser)
print('Test passed successfully!')