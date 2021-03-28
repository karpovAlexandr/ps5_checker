from telebot import TeleBot

try:
    from bot.settings import SHOPS, TOKEN, valid_chats
except ImportError:
    print(
        'you should create file "settings.py"\n'
        'at directory: "PS5_CHECKER/bot/" where\n'
        'SHOP - list of shops\n'
        'TOKEN - telegram bot TOKEN\n'
        'valid_chats - list of telegram chat id\'s with your bot'
    )
    SHOPS = []
    TOKEN = ''
    valid_chats = []
    exit()

sep = '\n'
app = TeleBot(__name__)


@app.route('(?!/).+')
def parrot(message):
    chat_id = message['chat']['id']
    if chat_id in valid_chats:
        msg = f"Привет!\n" \
              f"я слежу за наличием PlayStation 5 в следующих магазинах:\n" \
              f"{sep.join(SHOPS)}\n" \
              f"если ты видишь это сообщение, то значит ты в списке подписчиков"
    else:
        msg = "Привет!\n" \
              "Это частная вечеринка и здесь тебе не рады!"
    app.send_message(chat_id, msg)


def subscription_info(bot, text):
    bot.config['api_key'] = TOKEN
    for chat in valid_chats:
        bot.send_message(chat, text)


if __name__ == '__main__':
    app.config['api_key'] = TOKEN
    app.poll(debug=True)
