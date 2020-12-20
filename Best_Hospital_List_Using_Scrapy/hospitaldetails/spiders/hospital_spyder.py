# -*- coding: utf-8 -*-

import scrapy

from ..items import HospitaldetailsItem

class HospitalSpider(scrapy.Spider):
    name = 'hospital'
    page_number = 2
    start_urls = [
        'https://www.vaidam.com/hospitals/india?page=1'
        ]
    
    def parse(self,response):
        
        items =HospitaldetailsItem()
        
        # all_div_hospitals = response.css('div.item-list')
        
        # for hospitals in all_div_hospitals:
            
        name = response.css('.primary-heading-md a::text').extract()
        location = response.css('.primary-heading-md+ .clearfix::text').extract()
        no_of_beds = response.css('.fa-bed+ .font-bold::text').extract()
        hospital_type = response.css('.clearfix:nth-child(5)::text').extract()
        location = [x.strip() for x in location if len(x.strip())]
            
        for hospital in zip(name,location,no_of_beds,hospital_type):
            items['name'] = hospital[0]
            items['location'] = hospital[1]
            items['no_of_beds'] = hospital[2]
            items['hospital_type'] = hospital[3]
            yield items
            
        next_page = 'https://www.vaidam.com/hospitals/india?page='+str(HospitalSpider.page_number)
        
            
        if HospitalSpider.page_number < 6:
            
            HospitalSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
            
            