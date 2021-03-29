import requests
from bs4 import BeautifulSoup
from telebot import TeleBot

from bot.telegramBot import subscription_info
from settings.settings import HEADERS


class PageObject:
    HEADERS = HEADERS

    def __init__(self, name, url, html_element, css_class, html_text, test_url, encoding_type, email=False,
                 telegram=True, tests_on=True):
        self.name = name
        self.url = url
        self.encoding_type = encoding_type
        self.html_element = html_element
        self.html_text = html_text
        self.css_class = css_class
        self.test_url = test_url
        self.email = email
        self.telegram = telegram
        self.tests_on = tests_on

    def get_success_message(self, url):
        return f'I found some in {self.name}\n' \
               f'visit {url}'

    def get_failure_message(self):
        return f'There is no  PS5 in {self.name}'

    @staticmethod
    def send_bot_message(msg):
        app = TeleBot(__name__)
        subscription_info(app, msg)

    def run(self, url, encoding, test_run=False):
        try:
            result = requests.get(url, headers=self.HEADERS)
            result = result.content.decode(encoding=encoding)
            soup = BeautifulSoup(result, 'html.parser')
            button = soup.find_all(self.html_element, {"class": self.css_class})
            if button:
                msg = self.get_success_message(url)
                if not test_run:
                    self.send_bot_message(msg)
                return True, True
            else:
                msg = self.get_failure_message()
                print(msg)
                return True, False
        except Exception as exc:
            print(exc)
            return False, False

    def test(self):
        print(f'{self.name} test:')
        status, on_sale = self.run(self.test_url, self.encoding_type, test_run=True)
        print(f' - {self.name} - correct status {status}')
        print(f' - {self.name} - test good on sale {on_sale}')
        if not status or not on_sale:
            print(f'you need to change test URL: {self.test_url}')
            return False
        return True


if __name__ == '__main__':
    pass
