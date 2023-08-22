
import scrapy

class LinkedinProfilepider():

    #   name = 'scraper_profiles'

    def get_usernames(self):
        
        usernames = ['dolly-montoya-castaño-38918020']

        return usernames
    
    def start_requests(self):

        base_url = "https://www.linkedin.com/in/"

        usernames = self.get_usernames()


        for username in usernames : 
            profile_url = f"{base_url}{username}/"
            yield scrapy.Request(url=profile_url, callback=self.parse)

    def parse(self, response):
        # Utiliza selectores CSS para extraer información del perfil

        education_title = response.css('div.pvs-header__title-container h2.pvs-header__title::text').get()
        
        yield {
            'education_title': education_title,
        }
 

test = LinkedinProfilepider()

test.start_requests()