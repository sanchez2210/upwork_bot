import time
from selenium import webdriver
from query_manager import UpworkQueryManager
from bs4 import BeautifulSoup

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
                if self.is_captcha(self.driver.page_source):
                    input('Please solve the captcha type anything once done!: ')
                    time.sleep(2)
                    
                    
            except:
                pass
            
            else:
                not_loaded = False
            
            
            current_tries += 1
            
        if current_tries > self.max_tries:
            return None
        
        self.is_page_loaded = True
        return self.driver.page_source
        
    
    def change_query_manager(self, manager):
        self.is_page_loaded = False
        self.manager = manager
        
    
    def close_driver(self, ):
        self.driver.quit()
        
        
    def is_captcha(self, src):
        soup = BeautifulSoup(src, 'lxml')
        text = 'Please verify you are a human'
        h1 = soup.find('h1')
        if h1 and text in h1.text:
            return True
        return False

        

                
Bot = UpworkSeleniumBot




