# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:32:04 2020

@author: Piyush
"""
import random
import time
from bot import UpworkSeleniumBot
from query_manager import UpworkQueryManager
from upwork_scraper import UpworkScraper
from save_soup import save_soup




query = 'Software Developer'
num_pages = 2





def main():
    freelancers = list()
    manager = UpworkQueryManager(query, num_pages)
    urls = manager.get_all_urls()
    bot = UpworkSeleniumBot(manager)
    for url in urls:
        try:
            src = bot.get_source(url)
            scraper = UpworkScraper(src)
            freelancers +=scraper.get_freelance_details()
            
            
            
        except:
            pass
        time.sleep(random.uniform(1.8, 3.6))
        
#    bot.close_driver()
    
    return freelancers
    
    

