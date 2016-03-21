#!/usr/bin/env python
from os import environ
from telegram import Bot
from models import post

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logging.getLogger('requests').setLevel(logging.WARNING)
logger = logging.getLogger('@hardmob_promo')


def main():
    bot = Bot(environ.get('TOKEN'))
    chat_id = environ.get('CHAT_ID')

    post.updatedb()

    new_posts = post.get_posts(sent_only=False)

    if new_posts:
        logger.info('%d new post(s) to be sent!' % len(new_posts))
    else:
        logger.info('No new posts at this time!')

    for p in new_posts:
        bot.sendMessage(chat_id=chat_id, text=p.text(), parse_mode='HTML')
        post.mark_as_sent(p.uid)

if __name__ == '__main__':
    main()
