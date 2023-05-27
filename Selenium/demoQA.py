import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))
base_url = 'https://demoqa.com/date-picker'

browser.get(base_url)
browser.maximize_window()

# clear date input
calendar_input = browser.find_element(By.ID, value="datePickerMonthYearInput")
calendar_input.click()
calendar_input.send_keys(Keys.BACKSPACE*10)
time.sleep(3)

# convert date to UNIX format + 86400*10 seconds and convert new date to UTC format
now_date = datetime.today()
print(now_date)
unix_date = datetime.timestamp(now_date)
ten_days_later = unix_date + 864000
new_date = datetime.utcfromtimestamp(ten_days_later).strftime('%m/%d/%Y')
print(now_date)

# set new date in input
calendar_input.send_keys(new_date)
time.sleep(3)

browser.close()


# sys_date = datetime.utcnow().strftime('%d')
# date = int(sys_date) + 3
# locator = "//div[@aria-label='Choose Saturday, May " + str(date) + "th, 2023']"
# today = browser.find_element(By.XPATH, locator)
# today.click()
# time.sleep(3)

#today = browser.find_element(By.XPATH, value='//div[contains(@class,"react-datepicker__day--today")]')

# двойной клик и клик правой клавишей
# action = ActionChains(browser)
# checkbox = browser.find_element(by=By.ID, value="user-name")
# right_click = browser.find_element(by=By.ID, value="user-name")
# action.double_click(checkbox).perform()
# action.context_click(right_click).perform()
