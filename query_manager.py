class UpworkQueryManager:

    search_url = 'https://www.upwork.com/search/profiles/?q={}&page={}'
    
    
    
    def __init__(self, query, num_pages):
        self.query = query
        self.url_friendly_query = query.replace(' ', '+')
        self.num_pages = num_pages
    
    
    
    def get_query(self):
        return self.query
    
    def get_num_pages(self):
        return self.num_pages
    
    
    
    def get_url(self):
        return self.search_url.format(self.url_friendly_query, self.get_num_pages())
    
    
    def get_all_urls(self):
        urls = list()
        for i in range(1, self.num_pages + 1):
            urls.append(self.search_url.format(self.url_friendly_query, i))
        
        return urls
    

    def get_urls(self):
        pass
    
Manager = UpworkQueryManager

