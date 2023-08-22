import scrapy

class LinkedInSpider(scrapy.Spider):

    name = 'linkedin'
    start_urls = ['https://www.linkedin.com/search/results/people/?keywords=universidad%20nacional%20de%20colombia&origin=FACETED_SEARCH&schoolFilter=%5B%22464241%22%5D&sid=72-']  # Reemplaza con la URL del perfil que quieras buscar

    def parse(self, response):
        
        # Utiliza el selector CSS para obtener el contenedor deseado
        profile_container = response.css('li.reusable-search__result-container:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')

        # Extrae la información específica dentro del contenedor
        profile_name = profile_container.css('h3.name::text').get()
        profile_title = profile_container.css('p.subline-level-1::text').get()
        # Otros datos que quieras extraer...

        yield {
            'profile_name': profile_name,
            'profile_title': profile_title,
            # Otras variables...
        }