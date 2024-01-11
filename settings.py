import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')


BOT_NAME = 'DisplaySpecifications'

SPIDER_MODULES = ['DisplaySpecifications.spiders']
NEWSPIDER_MODULE = 'DisplaySpecifications.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DisplaySpecifications (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Crawl Once MIDDLEWARE
SPIDER_MIDDLEWARES = {
    # ...
    'scrapy_crawl_once.CrawlOnceMiddleware': 100,
    # ...
}

CRAWL_ONCE_ENABLED = True


DOWNLOADER_MIDDLEWARES = {
    'scrapy_crawl_once.CrawlOnceMiddleware': 50,
}

CONCURRENT_REQUESTS = 5

DOWNLOAD_TIMEOUT = 30000  # Increase this value if needed

PARAM = {
    # API Parameters
    # Set to 0 (off, default) or 1 (on) depending on whether or not to render JavaScript on the target web page. JavaScript rendering is done by using a browser.
    # 'render_js': 0,
    # Set datacenter (default) or residential depending on whether proxy type you want to use for your scraping request. Please note that a single residential proxy API request is counted as 25 API requests.
    #'proxy_type': 'datacenter',
    # Specify the 2-letter code of the country you would like to use as a proxy geolocation for your scraping API request. Supported countries differ by proxy type, please refer to the Proxy Locations section for details.
    # 'country': 'us',
    # Set depending on whether or not to use the same proxy address to your request.
    #'session': 1,
    # Specify the maximum timeout in milliseconds you would like to use for your scraping API request. In order to force a timeout, you can specify a number such as 1000. This will abort the request after 1000ms and return whatever HTML response was obtained until this point in time.
    # 'timeout': 10000,
    # Set desktop (default) or mobile or tablet, depending on whether the device type you want to your for your scraping request.
    # 'device': 'desktop',
    # Specify the option you would like to us as conditional for your scraping API request. Can only be used when the parameter render_js=1 is activated.
    # 'wait_until': 'domcontentloaded',
    # Some websites may use javascript frameworks that may require a few extra seconds to load their content. This parameters specifies the time in miliseconds to wait for the website. Recommended values are in the interval 5000-10000.
    # 'wait_for': 0,
}

# Mongodb Setting

MONGODB_SERVER = 'localhost'
MONGODB_SERVER_PORT = 27017
MONGODB_DATABASE = 'blackwidow_techspecs'
MONGODB_COLLECTION = 'devicespecifications-smartphones-tablets'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'DisplaySpecifications.middlewares.DisplayspecificationsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'DisplaySpecifications.middlewares.DisplayspecificationsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'DisplaySpecifications.pipelines.DisplayspecificationsPipeline': 300,
}

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
