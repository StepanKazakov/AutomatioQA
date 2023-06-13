import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

import main_project.pages.login_page
import main_project.pages.main_page
import main_project.pages.cart_page
import main_project.pages.client_page
import main_project.pages.payment_page
import main_project.pages.finish_button

def test_buy_product(set_up):

    browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))

    main_project.pages.login_page.NewLogin(browser).authorisation()

    main_project.pages.main_page.MainPage(browser).select_product()

    main_project.pages.cart_page.CartPage(browser).checkout()

    main_project.pages.client_page.ClientPage(browser).input_client_data()

    main_project.pages.payment_page.PaymentPage(browser).payment()

    main_project.pages.finish_button.Finish(browser).screenshot()
