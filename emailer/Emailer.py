import smtplib
import ssl


# TODO make "NORM" email
class Emailer:
    def __init__(self, email_server, port, login, password):
        self.email_server = email_server
        self.port = port
        self.login = login
        self.password = password
        self.context = None

    def get_context(self):
        self.context = ssl.create_default_context()

    @staticmethod
    def get_email_pattern(text):
        return f"{text}"

    def send_email(self, to, text):
        self.get_context()
        with smtplib.SMTP_SSL(self.email_server, self.port, context=self.context) as server:
            server.login(self.login, self.password)
            server.sendmail(from_addr=f'{self.login}@yandex.ru', to_addrs=to, msg=self.get_email_pattern(text))


if __name__ == '__main__':
    from settings.settings import SERVER, PORT
    from settings.sensitive_data import EMAIL

    e = Emailer(
        email_server=SERVER,
        port=PORT,
        login=EMAIL['login'],
        password=EMAIL['password']
    )
    e.send_email(
        to='karpov.a1exandr@yandex.ru',
        text='test_test_test'
    )
