

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
        print('Good value')

