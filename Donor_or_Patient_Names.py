from Scraper import PakistaniNamesScraper
import itertools

class PakistaniNamesGenerator:
    boys_url = "https://pakistaninames.wordpress.com/pakistani-boys-names/"
    girls_url = "https://pakistaninames.wordpress.com/pakistani-girls-names/"
    
    scraper = PakistaniNamesScraper(boys_url, girls_url)
    
    boys_names = scraper.get_boys_names()
    girls_names = scraper.get_girls_names()
    name2 = boys_names[::-1]
    
    @staticmethod
    def generate_male_full_names(boys_names, name2):
        male_full_names = []
        for boy, names in itertools.product(boys_names, name2):
            full_name = f'{boy} {names}'.replace(',', ' ')
            male_full_names.append(full_name)
        return male_full_names

    @staticmethod
    def generate_female_full_names(boys_names, girls_names):
        female_full_names = []
        for boy, girl in itertools.product(boys_names, girls_names):
            full_name = f'{girl} {boy}'.replace(',', ' ')
            female_full_names.append(full_name)
        return female_full_names
    @staticmethod
    def generate_full_names():
        boys_names = PakistaniNamesGenerator.boys_names
        girls_names = PakistaniNamesGenerator.girls_names
        name2 = PakistaniNamesGenerator.name2
    
        male_full_names = PakistaniNamesGenerator.generate_male_full_names(boys_names, name2)
        female_full_names = PakistaniNamesGenerator.generate_female_full_names(boys_names, girls_names)
    
        pakistani_names = []
        pakistani_names.extend(male_full_names)
        pakistani_names.extend(female_full_names)
    
        return pakistani_names


