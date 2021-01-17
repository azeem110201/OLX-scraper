# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CardekhoScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    score = scrapy.Field()
    is_new = scrapy.Field()
    is_hot = scrapy.Field()
    total_images = scrapy.Field()
    is_kyc_verified_user = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    created_at = scrapy.Field()
    title = scrapy.Field()
    car_body_type = scrapy.Field()
    main_info = scrapy.Field()
    display_date = scrapy.Field()
    user_id = scrapy.Field()
    price = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    region_id = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    varient = scrapy.Field()
    year = scrapy.Field()
    fuel = scrapy.Field()
    transmission = scrapy.Field()
    km = scrapy.Field()
    numberOfOwner = scrapy.Field()
    count = scrapy.Field()
