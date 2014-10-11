# -*- coding: utf-8 -*-

# Scrapy settings for app project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'app'

SPIDER_MODULES = ['app.spiders']
NEWSPIDER_MODULE = 'app.spiders'


DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 AppleWebKit/537.36 Chrome/27.0.1453.93 Safari/537.36'
COOKIES_ENABLED = False

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'log4crawlers.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False
