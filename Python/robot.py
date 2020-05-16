#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
from datetime import timedelta
import datetime

TELEGRAM_GROUP_ID = "-430620145"

TELEGRAM_BOT_TOKEN = "997581703:AAHkYozRSaMURQ6ZmYJAuvkcMbW_nc9HQLk"

LOG_PATH = os.path.dirname(os.path.realpath(__file__))+'/error.log'

yesterday = datetime.datetime.today() + timedelta(-1)
UPLOAD_FILE = '/data/www'
FILES = (
'admin-api-jobs-sx_server-%s.tar.gz' % yesterday.strftime('%Y-%m-%d'),
#'skynet-%s.tar.gz' % yesterday.strftime('%Y-%m-%d'),
)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def echo(bot, filename):
     try:
        fileobj = open(filename, 'rb')
        bot.send_document(chat_id=TELEGRAM_GROUP_ID, document=fileobj, timeout=30000)
        fileobj.close()
     except Exception as e:
        logging.error(e)
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    for index in FILES:
        echo(bot, "%s/%s" % (UPLOAD_FILE, index))


if __name__ == '__main__':
    main()
#status = os.system('sh /home/logs/delete.sh')
