import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

import main_project.pages.login_page
import main_project.pages.main_page

def test_menu_about():
    browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))

    print('start test')

    main_project.pages.login_page.NewLogin(browser).authorisation()

    main_project.pages.main_page.MainPage(browser).open_menu_about()


    time.sleep(1)
    print('The end')
