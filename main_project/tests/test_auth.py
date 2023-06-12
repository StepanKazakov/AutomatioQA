import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import main_project.pages.login_page

def test_auth():
    browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))

    print('start test')

    main_project.pages.login_page.NewLogin(browser).authorisation()

    time.sleep(3)
    print('The end')
