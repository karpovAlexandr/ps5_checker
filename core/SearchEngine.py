from core.PageObject import PageObject
from settings.settings import SHOPS


class SearchEngine:
    shops_base = SHOPS

    def __init__(self, telegram=True, email=True, tests_on=True, sleep=60):
        self.telegram = telegram
        self.email = email
        self.tests_on = tests_on
        self.sleep = sleep

    def run(self):
        for shop in self.shops_base.items():
            shop_page = PageObject(
                name=shop[0],
                telegram=self.telegram,
                email=self.email,
                tests_on=self.tests_on,
                **shop[1]
            )
            print(f'Checking {shop_page.name}...')
            if shop_page.test():
                shop_page.run(shop_page.url, shop_page.encoding_type)
            else:
                print(f'Something wrong with {shop_page.name}, just skip this shit')
            print('=======================================')
