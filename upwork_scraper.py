from bs4 import BeautifulSoup

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
                
            tile_name_col = profile.find('div', class_ = 'tile-name-col')

            profile_url = self.origin_url + tile_name_col.a.get('href') if tile_name_col and tile_name_col.find('a') else None
            
            title_class = 'ellipsis freelancer-tile-title_compact d-none d-md-block'

            title = profile.find('div', class_ = title_class).text if profile.find('div', class_ = title_class) else None

            for div in profile.find_all('div'):
                
                if div.attrs.get('data-rate'):
                    rate = div.text
                    rate = rate.replace('\xa0/ hr /hr', '').strip(' ')
                    rate_found = True
                    
                

                total_earnings = div.attrs.get('data-combined-earnings')

                total_hours = div.attrs.get('data-total-hours')
                
                if div.attrs.get('data-ng-if') and 'fullLocationLabel' in div.attrs.get('data-ng-if'):
                    country = div.text
                    country_found = True

                
                
            
            if not country_found:
                country = None
            
            if not rate_found:
                rate = None
                
            

            if get_all_details:

                freelancer_details['country'] = country

                freelancer_details['total_hours'] = total_hours

                freelancer_details['rate'] = rate

                freelancer_details['title'] = title

                freelancer_details['total_earnings'] = total_earnings

                freelancer_details['profile_url'] = profile_url

                freelancer_details['name'] = name


            else:
                freelancer_details['name'] = name

                freelancer_details['title'] = title

                freelancer_details['rate'] = rate

                freelancer_details['profile_url'] = profile_url

            freelancers_details.append(freelancer_details)


        return freelancers_details



