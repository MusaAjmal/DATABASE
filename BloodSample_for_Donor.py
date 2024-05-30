from faker import Faker
from faker.providers import DynamicProvider

class BloodSample:
    def __init__(self):
        self.faker = Faker()
        resultProvider = DynamicProvider(
            provider_name="Results",
            elements=['+', '-']
        )
        self.faker.add_provider(resultProvider)
    def insert(self):
         data={}
         data["id"]=self.sample_id = self.faker.unique.random_int(min=1, max=2147483647)
         data["results"]=self.results = self.faker.Results()
         return data
        
   
