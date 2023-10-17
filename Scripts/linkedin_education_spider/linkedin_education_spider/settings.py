# Scrapy settings for linkedin_education_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "linkedin_education_spider"

SPIDER_MODULES = ["linkedin_education_spider.spiders"]
NEWSPIDER_MODULE = "linkedin_education_spider.spiders"

# HTTPCACHE_ENABLED = True

# Obey robots.txt rules
ROBOTSTXT_OBEY = False



SCRAPEOPS_API_KEY = 'e48ab866-0125-4825-b9ad-1d397d58e983' #'4763efcd-a470-45cd-a742-f3fda6e5dffc' #'4763efcd-a470-45cd-a742-f3fda6e5dffc' #'9f31ce1d-7f22-4ff2-b314-9c102eeae2c3'#'48d6cd4d-3476-414f-8fb4-f64539330026'



# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}


DOWNLOADER_MIDDLEWARES = {

    ## ScrapeOps Monitor
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    
    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1