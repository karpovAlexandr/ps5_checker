import random

"""
    url - ссылка на страничку товара -> str
    encoding_type -  тип энкодинга (прим. utf8) - > str
    html_element - название html элемента, наличие которого  говорит о наличии -> str
    html_text - текс в html элементе или значение value -> str
    css_class - css свойства html элемента -> str
    test_url - ссылка для теста работы -> str
    пример ниже:
"""
SHOPS = {
    'mvideo': {
        'url': 'https://www.mvideo.ru/products/igrovaya-konsol-sony-playstation-5-40073270',
        'encoding_type': 'utf8',
        'html_element': 'input',
        'html_text': 'Добавить в корзину',
        'css_class': 'add-to-basket-button',
        'test_url': 'https://www.mvideo.ru/products/geimpad-sony-playstation-5-dualsense-cfi-zct1w-40074732',
    },

}

"""
    можно добавить свой user-agent, один или несколько
"""

USER_AGENTS = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 '
               'YaBrowser/20.2.3.320 (beta) Yowser/2.5 Safari/537.36']

HEADERS = {
    'User-Agent': random.choice(USER_AGENTS)
}
