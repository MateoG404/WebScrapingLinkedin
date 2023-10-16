import scrapy

class LinkedInSpider(scrapy.Spider):
    name = 'linkedin_login'
    
    # Initial request to login page
    def start_requests(self):
        urls = ['https://www.linkedin.com/login']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_login)
            
    # Login process using POST request
    def parse_login(self, response):
        pasw = "c&'n~yuA3faM2Tr"
        return scrapy.FormRequest.from_response(
            response,
            formdata={'session_key': 'xineb45323@dixiser.com', 'session_password': pasw},
            callback=self.after_login
        )
    
    # Verify login succeeded and navigate to the profile page
    def after_login(self, response):
        if 'authentication failed' in str(response.body):
            self.logger.error('Login failed.')
            return
        else:
            self.logger.info('Login succeeded.')
            next_page = 'https://www.linkedin.com/in/mateo-gutiérrez-melo-389996209/'
            yield scrapy.Request(url=next_page, callback=self.parse_profile)
    
    # Parse profile page (just an example)
    def parse_profile(self, response):
        self.logger.info('Visited %s', response.url)
        with open('profile.html', 'wb') as f:
            f.write(response.body)
