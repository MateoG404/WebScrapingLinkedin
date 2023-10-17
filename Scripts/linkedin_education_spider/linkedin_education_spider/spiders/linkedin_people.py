import scrapy
import pandas as pd
from .linkedin_links import LinkedinLinks

class LinkedInPeopleProfileSpider(scrapy.Spider):
    name = "linkedin_people_profile"

    custom_settings = {
        'FEEDS': { 'data/%(name)s_%(time)s.jsonl': { 'format': 'jsonlines',}}
            }
    def get_profile_list(self,file_path):
        try:
            # Read the Excel file into a DataFrame
            df = pd.read_excel(file_path)
            
            # Check for the existence of the 'URL' column
            if 'URL' not in df.columns:
                print("Error: 'URL' column not found.")
                return None

            # Extract URLs and store them in a list
            url_list = df['URL'].dropna().tolist()

            return url_list

        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    
    def start_requests(self):

        #['josé-ismael-peña-reyes-5ab68143','dolly-montoya-castaño-38918020','reidhoffman','mateo-gutiérrez-melo-389996209','juanwilchesmadlies','desarrollósoluciones']
        #obj = LinkedinLinks()
        
        #profile_list = obj.get_profiles()
        
        #profile_list = profile_list[:2]

        #profile_list = ['mateo-gutiérrez-melo-389996209']#['fabian-antonio-perez-arias-42226616a']
        profile_list = ['diana-milena-rivera-g']
        linkedin_urls = ['https://www.linkedin.com/in/sebastian-garcia-031629122/', 'https://www.linkedin.com/in/juan-carlos-zambrano-48a34311/?locale=en_US', 'https://www.linkedin.com/in/sebasti%C3%A1n-rosas-barahona-3213b9159/', 'https://www.linkedin.com/in/angie-lorena-galvis-lara-a45a19141/', 'https://www.linkedin.com/in/andr%C3%A9s-felipe-vega-27072042/', 'https://www.linkedin.com/in/edgar-fernando-duarte-herrera-5425b9b4/', 'https://www.linkedin.com/in/carlos-david-pulido-bonilla-81270a52/', 'https://www.linkedin.com/in/felipe-escobar-0a704919a/', 'https://www.linkedin.com/in/jorge-casta%C3%B1o-a9120095/?original_referer=https%3A%2F%2Fwww.google.com%2F', 'https://www.linkedin.com/in/natalia-tello-quiroz-a06a99211/?originalSubdomain=co', 'https://www.linkedin.com/in/juan-guillermo-rute-sanabria-2a683158/?originalSubdomain=es']


        for profile in linkedin_urls:
            
            #linkedin_people_url = f'https://www.linkedin.com/in/{profile}/' 
            linkedin_people_url = profile
            yield scrapy.Request(url=linkedin_people_url, callback=self.parse_profile, meta={'profile': profile, 'linkedin_url': linkedin_people_url})


    def parse_profile(self, response):
        item = {}
        item['profile'] = response.meta['profile']
        item['url'] = response.meta['linkedin_url']

        """
            SUMMARY SECTION
        """
        summary_box = response.css("section.top-card-layout")
        item['name'] = summary_box.css("h1::text").get().strip()
        item['description'] = summary_box.css("h2::text").get().strip()

        ## Location
        try:
            item['location'] = summary_box.css('div.top-card__subline-item::text').get()
        except:
            item['location'] = summary_box.css('span.top-card__subline-item::text').get().strip()
            if 'followers' in item['location'] or 'connections' in item['location']:
                item['location'] = ''

        item['followers'] = ''
        item['connections'] = ''

        for span_text in summary_box.css('span.top-card__subline-item::text').getall():
            if 'followers' in span_text:
                item['followers'] = span_text.replace(' followers', '').strip()
            if 'connections' in span_text:
                item['connections'] = span_text.replace(' connections', '').strip()


        """
            ABOUT SECTION
        """
        item['about'] = response.css('section.summary div.core-section-container__content p::text').get()


        """
            EXPERIENCE SECTION
        """
        item['experience'] = []
        experience_blocks = response.css('li.experience-item')
        for block in experience_blocks:
            experience = {}
            ## organisation profile url
            try:
                experience['organisation_profile'] = block.css('h4 a::attr(href)').get().split('?')[0]
            except Exception as e:
                print('experience --> organisation_profile', e)
                experience['organisation_profile'] = ''
                
                
            ## location
            try:
                experience['location'] = block.css('p.experience-item__location::text').get().strip()
            except Exception as e:
                print('experience --> location', e)
                experience['location'] = ''
                
                
            ## description
            try:
                experience['description'] = block.css('p.show-more-less-text__text--more::text').get().strip()
            except Exception as e:
                print('experience --> description', e)
                try:
                    experience['description'] = block.css('p.show-more-less-text__text--less::text').get().strip()
                except Exception as e:
                    print('experience --> description', e)
                    experience['description'] = ''
                    
            ## time range
            try:
                date_ranges = block.css('span.date-range time::text').getall()
                if len(date_ranges) == 2:
                    experience['start_time'] = date_ranges[0]
                    experience['end_time'] = date_ranges[1]
                    experience['duration'] = block.css('span.date-range__duration::text').get()
                elif len(date_ranges) == 1:
                    experience['start_time'] = date_ranges[0]
                    experience['end_time'] = 'present'
                    experience['duration'] = block.css('span.date-range__duration::text').get()
            except Exception as e:
                print('experience --> time ranges', e)
                experience['start_time'] = ''
                experience['end_time'] = ''
                experience['duration'] = ''
            
            item['experience'].append(experience)

        
        """
            EDUCATION SECTION
        """
        item['education'] = []
        education_blocks = response.css('li.education__list-item')
        for block in education_blocks:
            education = {}

            ## organisation
            try:
                education['organisation'] = block.css('h3::text').get().strip()
            except Exception as e:
                print("education --> organisation", e)
                education['organisation'] = ''


            ## organisation profile url
            try:
                education['organisation_profile'] = block.css('a::attr(href)').get().split('?')[0]
            except Exception as e:
                print("education --> organisation_profile", e)
                education['organisation_profile'] = ''

            ## course details
            try:
                education['course_details'] = ''
                for text in block.css('h4 span::text').getall():
                    education['course_details'] = education['course_details'] + text.strip() + ' '
                education['course_details'] = education['course_details'].strip()
            except Exception as e:
                print("education --> course_details", e)
                education['course_details'] = ''

            ## description
            try:
                education['description'] = block.css('div.education__item--details p::text').get().strip()
            except Exception as e:
                print("education --> description", e)
                education['description'] = ''

         
            ## time range
            try:
                date_ranges = block.css('span.date-range time::text').getall()
                if len(date_ranges) == 2:
                    education['start_time'] = date_ranges[0]
                    education['end_time'] = date_ranges[1]
                elif len(date_ranges) == 1:
                    education['start_time'] = date_ranges[0]
                    education['end_time'] = 'present'
            except Exception as e:
                print("education --> time_ranges", e)
                education['start_time'] = ''
                education['end_time'] = ''

            item['education'].append(education)

        yield item

       
#obj = LinkedInPeopleProfileSpider()
#print(obj.get_profile_list('/home/user/Desktop/MateoCodes/WebScrapingLinkedin/documentacion/copy/df_limpio.xlsx'))
