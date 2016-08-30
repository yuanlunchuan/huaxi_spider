# -*- coding: utf-8 -*-
import scrapy

class HuaxiDoctorItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    major = scrapy.Field()
