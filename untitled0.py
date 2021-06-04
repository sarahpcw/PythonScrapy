# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:09:38 2020

@author: u
"""

import scrapy 
from scrapy.item import Item, Field 


class FirstSpider(scrapy.Spider): 
   name = "first" 
   
   def __init__(self, group = None, *args, **kwargs): 
      super(FirstSpider, self).__init__(*args, **kwargs) 
      self.start_urls = ["http://www.example.com/group/%s" % group]

  
class First_scrapyItem(scrapy.Item): 
   product_title = Field() 
   product_link = Field() 
   product_description = Field() 