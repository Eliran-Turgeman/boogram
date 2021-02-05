from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat.id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def get_token():
    with open("token.txt") as f:
        token = f.read().strip()
    return token


def main():
    updater = Updater(get_token())
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()