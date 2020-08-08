import time
from selenium import webdriver
from query_manager import UpworkQueryManager


class UpworkSeleniumBot:
    driver_path = 'C:\Program Files (x86)\chromedriver.exe'
    max_tries = 3
    def __init__(self, query_manager):
        self.manager = query_manager
        self.query = query_manager.get_query()
        self.driver = webdriver.Chrome(self.driver_path)
        is_page_loaded = False
    
    def get_source(self, url = None):
        current_tries = 0
        not_loaded = True
        if url == None:
            url = self.manager.get_url()
            
        while current_tries <= self.max_tries and not_loaded:
            try:
                self.driver.get(url)
            except:
                pass
            
            else:
                not_loaded = False
            
            
            current_tries += 1
            
        if current_tries > self.max_tries:
            return None
        
        time.sleep(1.5)
        self.is_page_loaded = True
        return self.driver.page_source
        
    
    def change_query_manager(self, manager):
        self.is_page_loaded = False
        self.manager = manager
        
    
    def close_driver(self, ):
        self.driver.quit()

                
Bot = UpworkSeleniumBot




