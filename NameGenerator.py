from Scraper import PakistaniNamesScraper
import itertools

boys_url = "https://pakistaninames.wordpress.com/pakistani-boys-names/"
girls_url = "https://pakistaninames.wordpress.com/pakistani-girls-names/"


scraper = PakistaniNamesScraper(boys_url, girls_url)

boys_names = scraper.get_boys_names()
girls_names = scraper.get_girls_names()
name2= name2 = boys_names[::-1]

def generate_male_full_names(boys_names, name2):
    male_full_names = []
    for boy, names in itertools.product(boys_names, name2):
        full_name = f'{boy} {names}'.replace(',', ' ')
        male_full_names.append(full_name)
    return male_full_names

def generate_female_full_names(boys_names, girls_names):
    female_full_names = []
    for boy, girl in itertools.product(boys_names, girls_names):
        full_name = f'{girl} {boy}'.replace(',', ' ')
        female_full_names.append(full_name)
    return female_full_names

male_full_names = generate_male_full_names(boys_names,name2)
female_full_names = generate_female_full_names(boys_names, girls_names)
Pakistani_Names=[]
Pakistani_Names.extend(male_full_names)
Pakistani_Names.extend(female_full_names)
print(Pakistani_Names)
