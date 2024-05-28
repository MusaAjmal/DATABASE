import requests
from bs4 import BeautifulSoup

class PakistaniNamesScraper:
    def __init__(self, boys_url, girls_url):
        self.boys_url = boys_url
        self.girls_url = girls_url

    def scrape_names(self, url):
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        post_div = soup.find('div', id='post-3' if 'boys' in url else 'post-4')
        ul_inside_post = post_div.find('ul')
        name_items = ul_inside_post.find_all('li')
        names = [item.text.split(':', 1)[-1].split('/', 1)[0].strip() for item in name_items if "(Alexander)" not in item.text and '/' in item.text]

        #names = [item.text.split(':', 1)[-1].split('/', 1)[0].strip() for item in name_items if "(Alexander)" not in item.text] 
        #names = [item.text.split(':', 1)[-1].strip() for item in name_items if "(Alexander)" not in item.text]
        #names = [item.text.split(':', 1)[-1].strip() for item in name_items if item not "(Alexander)"]
        non_empty_list = [value for value in names if value]
        names_string = ' '.join(non_empty_list)
        return names_string.split()

    def get_boys_names(self):
        return self.scrape_names(self.boys_url)

    def get_girls_names(self):
        return self.scrape_names(self.girls_url)

boys_url = "https://pakistaninames.wordpress.com/pakistani-boys-names/"
girls_url = "https://pakistaninames.wordpress.com/pakistani-girls-names/"

scraper = PakistaniNamesScraper(boys_url, girls_url)

boys_names = scraper.get_boys_names()
girls_names = scraper.get_girls_names()

