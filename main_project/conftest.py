import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService



@pytest.fixture()
def set_up():
    print('start test')
    browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
    url = 'https://www.saucedemo.com'
    self.browser.get(self.url)
    self.browser.maximize_window()

    yield

    browser.quit()
    print('finish test')

@pytest.fixture(scope='module')
def set_group():
    print('start system')

    yield

    print('exit system')