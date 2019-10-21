# -*- coding: utf-8 -*-

# Scrapy settings for behance project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'behance'

SPIDER_MODULES = ['behance.spiders']
NEWSPIDER_MODULE = 'behance.spiders'

MAX_PAGE = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'behance (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Host': 'www.behance.net',
    'X-Requested-With': 'XMLHttpRequest',
    'X-BCP': '141fe6a8-d820-4f83-b4e7-b163d9c4bcea',
    'Cookie': 'gk_suid=28673185; gki=%7B%22db_semaphore%22%3Afalse%2C%22live_featured_hero%22%3Afalse%7D; bcp=141fe6a8-d820-4f83-b4e7-b163d9c4bcea; bcp_generated=1571629359737; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=-227196251%7CMCMID%7C72889074359490452383631747725102698294%7CMCAAMLH-1572234171%7C11%7CMCAAMB-1572234171%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1571636571s%7CNONE%7CMCAID%7CNONE; s_sess=%20s_dmdbase%3D1%3B%20s_dmdbase_custom%3D1%3B%20s_cpc%3D0%3B%20s_sq%3D%3B%20s_ppv%3D%255B%2522www.behance.net%252Fgalleries%252Fphotography%2522%252C100%252C0%252C5139%252C1707%252C569%252C1707%252C960%252C1.5%252C%2522P%2522%255D%3B%20s_cc%3Dtrue%3B; s_pers=%20s_nr%3D1571629834624-New%7C1603165834624%3B%20cpn%3Dbehance.net%253Agalleries%7C1729482634745%3B%20ppn%3Dbehance.net%253Agallery%7C1729482634746%3B%20s_vs%3D1%7C1571633339745%3B'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'behance.middlewares.BehanceSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'behance.middlewares.BehanceDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'behance.pipelines.DetailPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
