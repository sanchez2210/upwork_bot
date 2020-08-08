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
import json
from datetime import datetime


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
    
#    return freelancers
    
    now = datetime.now()
    timestamp = now.strftime("%d_%b_%Y_time_%H_%M_%p")
    
    directory = 'assets/'
    
    file_name = query + '_' + timestamp + '.txt'
    
    file_path = directory + file_name
    
    JSON = json.dumps(freelancers)
    with open(file_path, 'w') as f:
        f.write(JSON)
        print('File: %s written successfully...' % (file_name))
        

    
    return JSON





