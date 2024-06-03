from faker import Faker
from datetime import date

class Transfusions:
    def __init__(self):
        self.faker=Faker()
        
    def generate(self):
        data={}
        data['id']=self.faker.unique.random_int(min=1111111111, max=2147483647)
        start=date.today()
        data['startdate']=start.strftime("%Y-%m-%d")
        return data


#Test Object



