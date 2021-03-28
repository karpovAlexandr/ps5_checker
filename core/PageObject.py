import requests
from bs4 import BeautifulSoup
from telebot import TeleBot

from bot.telegramBot import subscription_info
from settings.settings import HEADERS
from settings.settings import SERVER, PORT
from emailer.Emailer import Emailer

try:
    from settings.sensitive_data import EMAIL, TO

    login = EMAIL.get('login')
    password = EMAIL.get('password')

except ImportError:
    print(
        'you should create file "sensitive_data.py"\n'
        'at directory: "APP_PATH/settings/" where\n'
        'EMAIL - dict with keys:\n'
        'login - your yandex email login (not email)\n'
        'password  - your password\n'
        'you also can edit APP_PATH/emailer/Emailer.py for your needs'
    )
    EMAIL = {}
    login = ''
    password = ''
    TO = ''
    exit()

emailer = Emailer(
    email_server=SERVER,
    port=PORT,
    login=login,
    password=password
)


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
    def send_mail(msg):
        emailer.send_email(to=TO, text=msg)

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
                    if self.email:
                        self.send_mail(msg)
                    if self.telegram:
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
    emailer.send_email(to=TO, text='test')
