# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HospitaldetailsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()
    location = scrapy.Field()
    no_of_beds = scrapy.Field()
    hospital_type = scrapy.Field()
    
