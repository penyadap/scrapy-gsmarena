# -*- coding: utf-8 -*-

# Scrapy settings for book_data_item_loader project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gsmarenakun'

SPIDER_MODULES = ['gsmarenakun.spiders']
NEWSPIDER_MODULE = 'gsmarenakun.spiders'

# LOG_STDOUT = True
# LOG_FILE = './tmp/scrapy_output.txt'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'book_data_item_loader (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,

    # ...
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
    # ...
}

# ROTATING_PROXY_LIST = [
#     '178.128.221.243:26323',
#     '139.162.102.215:38118',
#     # ...
# ]

FAKEUSERAGENT_PROVIDERS = [
    # This is the first provider we'll try
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',
    # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FakerProvider',
    # Fall back to USER_AGENT value
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',
]
