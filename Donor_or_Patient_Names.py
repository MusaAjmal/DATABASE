from Scraper import PakistaniNamesScraper
import itertools

class PakistaniNamesGenerator:
    def __init__(self, boys_url, girls_url):
        self.boys_url = boys_url
        self.girls_url = girls_url
        self.scraper = PakistaniNamesScraper(boys_url, girls_url)
        self.pakistani_names = self.generate_all_names()

    def generate_male_full_names(self, boys_names, reversed_boys_names):
        male_full_names = []
        for boy, names in itertools.product(boys_names, reversed_boys_names):
            full_name = f'{boy} {names}'.replace(',', ' ')
            male_full_names.append(full_name)
        return male_full_names

    def generate_female_full_names(self, boys_names, girls_names):
        female_full_names = []
        for boy, girl in itertools.product(boys_names, girls_names):
            full_name = f'{girl} {boy}'.replace(',', ' ')
            female_full_names.append(full_name)
        return female_full_names

    def generate_all_names(self):
        boys_names = self.scraper.get_boys_names()
        girls_names = self.scraper.get_girls_names()
        reversed_boys_names = boys_names[::-1]

        male_full_names = self.generate_male_full_names(boys_names, reversed_boys_names)
        female_full_names = self.generate_female_full_names(boys_names, girls_names)

        all_names = male_full_names + female_full_names
        return all_names

    def get_name_count(self):
        return len(self.pakistani_names)

# Usage
boys_url = "https://pakistaninames.wordpress.com/pakistani-boys-names/"
girls_url = "https://pakistaninames.wordpress.com/pakistani-girls-names/"

generator = PakistaniNamesGenerator(boys_url, girls_url)
print(generator.pakistani_names)
