import datetime


class Base():

    def __init__(self, browser):
        self.browser = browser

# get base url
    def get_current_url(self):
        get_url = self.browser.current_url
        print('url = ' + get_url)

# check success authorisation
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value title')

# take screenshot success
    def get_screenshot(self):
        sys_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M')
        name_screen = 'screen' + sys_date + '.png'
        self.browser.save_screenshot('/Users/stef/PycharmProjects/AutomatioQA/'
                                     'main_project/screen/' + name_screen)

    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print('Good value URL')