#!/usr/bin/env python
from os import environ
from telegram import Bot
from models import post


def main():
    bot = Bot(environ.get('TOKEN'))
    chat_id = environ.get('CHAT_ID')

    post.updatedb()

    for p in post.get_posts(sent_only=False):
        bot.sendMessage(chat_id=chat_id, text=p.text(), parse_mode='HTML')
        post.mark_as_sent(p.uid)

if __name__ == '__main__':
    main()
