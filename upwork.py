#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests_module import Request
from bs4 import BeautifulSoup
from save_soup import save_soup
from selenium import webdriver
bs = BeautifulSoup


# In[2]:


import time


# In[3]:


path = "C:\Program Files (x86)\chromedriver.exe"


# In[4]:


driver = webdriver.Chrome(path)


# In[11]:


url = 'https://www.upwork.com/search/profiles/?q=software%20developer'


# In[12]:


driver.get(url)


# In[14]:


src = driver.page_source


# In[ ]:





# In[15]:


soup  = bs(src, 'lxml')


# # Getting name

# In[ ]:





# In[18]:


profiles = soup.find_all('article')


# In[19]:


profile = profiles[0]


# In[55]:


profile_divs = profile.find_all('div')


# In[37]:


title_name_div = 'tile-name-col'


# In[45]:


profile.find('div', class_ = title_name_div).span.text


# # profile link

# In[48]:


profile.find('div', class_ = title_name_div).a['href']


# # Title

# In[49]:


div_title_class = 'ellipsis freelancer-tile-title_compact d-none d-md-block'


# In[51]:


profile.find('div', class_ = div_title_class).text


# # OR another way is

# In[54]:


profile.find('strong').text


# # Getting hourly rate

# In[60]:


for div in profile_divs:
    if div.attrs.get('data-rate'):
        print(div.text)


# # combined earingnigs

# In[64]:


for div in profile_divs:
    if div.attrs.get('data-combined-earnings'):
        print(div.attrs.get('data-combined-earnings'))


# # Total hours

# In[67]:


for div in profile_divs:
    if div.attrs.get('data-total-hours'):
        print(div.attrs.get('data-total-hours'))


# # Description

# In[71]:


for div in profile_divs:
    if div.attrs.get('data-ng-if') and 'freelancer.description' in div.attrs.get('data-ng-if'):
        print(div.text)


# # country

# In[74]:


for div in profile_divs:
    if div.attrs.get('data-ng-if') and 'fullLocationLabel' in div.attrs.get('data-ng-if'):
        print(div.text)


# In[ ]:





# # skills

# In[15]:


class UpworkScraper:
    
    origin_url = 'https://www.upwork.com'
    
    def __init__(self, src):
        self.src = src
        
    def get_soup(self):
        return BeautifulSoup(self.src, 'lxml')
    
    def get_freelance_details(self, get_all_details = False):
        freelancers_details = list()
        
        soup = self.get_soup()
        
        profiles = soup.find_all('article')
        
        for profile in profiles:
            freelancer_details = dict()
            name_span = profile.find('div', class_ = 'tile-name-col').span if profile.find('div', class_ = 'tile-name-col') else None
            name = name_span.text if name_span else None
            freelancer_detials['name'] = name_span.text if name_span else None
                
                
            tile_name_col = profile.find('div', class_ = 'tile-name-col')
            profile_url = tile_name_col.a.get['href'] if tile_name_col and 'a' in tile_name_col.attrs else None
            freelancer_details['profile_url'] = tile_name_col.a.get['href'] if tile_name_col and 'a' in tile_name_col.attrs else None
            
            
            title_class = 'ellipsis freelancer-tile-title_compact d-none d-md-block'
            title = profile.find('div', class_ = title_class).text if profile.find('div',class_ = title_class) else None
            freelancer_details['title'] = profile.find('div', class_ = title_class).text if profile.find('div',class_ = title_class) else None
            
            
            for div in profile.find_all('div'):
                rate = div.text if div.attrs.get('data-rate') else None
                
                freelancer_details['rate'] = div.text if div.attrs.get('data-rate') else None
                
                total_earnings = div.attrs.get('data-combined-earnings')
                
                freelancer_details['total_earnings'] = div.attrs.get('data-combined-earnings')
                
                total_hours = div.attrs.get('data-total-hours')
                
                freelancer_details['total_hours'] = div.attrs.get('data-total-hours')
                
                country = div.text if div.attrs.get('data-ng-if') and 'fullLocationLabel' in div.attrs.get('data-ng-if') else None
                
                freelancer_details['country'] = div.text if div.attrs.get('data-ng-if') and 'fullLocationLabel' in div.attrs.get('data-ng-if') else None
                
                
                
                
                    
                
                
                
                


# In[77]:


ul = profile.find('ul', class_ = 'skill-list-light')


# In[81]:


for li in ul.find_all('li'):
    print(li.span.text) if li.span else print(None)


# In[ ]:





# In[93]:


url


# # Selenium Scraper

# In[107]:


class UpworkQueryManager:
    
    search_url = 'https://www.upwork.com/search/profiles/?q={}'
    
    
    
    def __init__(self, query, num_pages):
        self.query = query
        self.url_friendly_query = query.replace(' ', '+')
        self.num_pages = num_pages
    
    
    
    def get_query(self):
        return self.query
    
    def get_num_pages(self):
        return self.num_pages
    
    
    
    def get_url(self):
        return self.search_url.format(self.url_friendly_query)
    
    
Manager = UpworkQueryManager


# In[120]:


class UpworkSeleniumBot:

    
    def __init__(self, query_manager):
        self.manager = query_manager
        self.query = query_manager.get_query()
        self.driver = webdriver.Chrome(path)
        is_page_loaded = False
    
    def get_source(self, url = None):
        if url == None:
            url = manager.get_url()
        self.driver.get(url)
        time.sleep(1.5)
        self.is_page_loaded = True
        return self.driver.page_source
        
    
    def change_query_manager(self, manager):
        self.is_page_loaded = False
        self.manager = manager
        
    
    def close_driver(self, ):
        pass

                
Bot = UpworkSeleniumBot


# In[117]:


manager = Manager('software', 2)


# In[121]:


bot = Bot(manager)


# In[122]:


bot.get_source()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[34]:


for div in profile.find_all('div'):
    print(div.attrs.get('class'))
    print('============')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


resp = Request.get(url)


# In[6]:


save_soup(resp)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




