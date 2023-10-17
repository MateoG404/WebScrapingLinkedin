
'''
import defer
import pandas as pd
from twisted.internet import reactor
from scrapy.settings import CrawlRunner
from linkedin_links import LinkedinLinks
from linkedin_education_spider import LinkedInPeopleProfileSpider

# Initialize LinkedinLinks object and read data
obj = LinkedinLinks()
df_data = obj.returnDataForBot()

# Initialize CrawlRunner
runner = CrawlRunner()

# Asynchronous crawling
crawls = []
for _, column in df_data.head(2).iterrows():  # Limited to first 2 rows for testing
    profile_name = obj.get_profile(column['URL'])
    crawl = runner.crawl(LinkedInPeopleProfileSpider, profile=profile_name)
    crawls.append(crawl)

# Wait for all crawls to complete
d = defer.DeferredList(crawls)
d.addBoth(lambda _: reactor.stop())

# Start the reactor
reactor.run()



for i in range(1, 101):
    
    command = "scrapy crawl linkedin_login -o moco.json"
    subprocess.run(command, shell=True)
'''