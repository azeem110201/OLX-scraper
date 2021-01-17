import scrapy
from ..items import CardekhoScrapeItem

base_url = "https://www.olx.in/api/relevance/v2/search?facet_limit=100&lang=en&location=4058526&location_facet_limit=20&page={}&platform=web-desktop&query=cars&spellcheck=true&user=176ff8513b8x68251939"
class CardekhoSpider(scrapy.Spider):
    name = 'cardekho'
    start_page = 1
    start_urls = [
        base_url.format(0)
    ]

    def parse(self, response):
        items = CardekhoScrapeItem()
        data = response.json()
        for i in range(len(data['data'])):
            items['id'] = data['data'][i]['id']
            items['score'] = data['data'][i]['score']
            try:
                items['is_new'] = data['data'][i]['status']['flags']['new']
                items['is_hot'] = data['data'][i]['status']['flags']['hot']
            except:
                items['is_new'] = "None"
                items['is_hot'] = "None"

            try:
                items['is_kyc_verified_user'] = data['data'][i]['is_kyc_verified_user']
            except:
                items['is_kyc_verified_user'] = "None"            

            try:
                items['state'] = data['data'][i]['locations_resolved']['ADMIN_LEVEL_1_name']
            except:
                items['state'] = "None"

            try:
                items['city'] = data['data'][i]['locations_resolved']['ADMIN_LEVEL_3_name']
            except:
                items['city'] = "None"

            try:
                items['location'] = data['data'][i]['locations_resolved']['SUBLOCALITY_LEVEL_1_name']
            except:
                items['location'] = "None"

            try:
                items['description'] = data['data'][i]['description'].strip()
            except:
                items['description'] = "None"

            try:
                items['title'] = data['data'][i]['title']
            except:
                items['title'] = "None"

            try:
                items['car_body_type'] = data['data'][i]['car_body_type']
            except:
                items['car_body_type'] = "None"

            try:
                items['main_info'] = data['data'][i]['main_info']
            except:
                items['main_info'] = "None"

            try:
                items['price'] = data['data'][i]['price']['value']['raw']
            except:
                items['price'] = 0       

            items['created_at'] = data['data'][i]['created_at']
            
            items['display_date'] = data['data'][i]['display_date']
            items['user_id'] = data['data'][i]['user_id']
            items['lat'] = data['data'][i]['locations'][0]['lat']
            items['lon'] = data['data'][i]['locations'][0]['lon']
            ##count
            #items['count'] = len(data['data'][i]['parameters'][0])
            #count ends
            items['region_id'] = data['data'][i]['locations'][0]['region_id']
            for _ in range(len(data['data'][i]['parameters'])):
                k = 0
                try:
                    items['brand'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['brand'] = "None"
                k += 1
                try:
                    items['model'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['model'] = "None"  
                k += 1    
                try:
                    items['varient'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['varient'] = "None"
                k += 1
                try:
                    items['year'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['year'] = "None"
                k += 1
                try:
                    items['fuel'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['fuel'] = "None"
                k += 1
                try:
                    items['transmission'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['transmission'] = "None"     
                k += 1
                try:
                    items['km'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['km'] = "None"
                k += 1
                try:
                    items['numberOfOwner'] = data['data'][i]['parameters'][k]['value_name']
                except:
                    items['numberOfOwner'] = "None"                   


            yield items

        next_page = 'https://www.olx.in/api/relevance/v2/search?facet_limit=100&lang=en&location=4058526&location_facet_limit=20&page=' + str(CardekhoSpider.start_page) + '&platform=web-desktop&query=cars&spellcheck=true&user=176ff8513b8x68251939'
        if CardekhoSpider.start_page <= 49:
            CardekhoSpider.start_page += 1
            yield response.follow(next_page, callback=self.parse)    