from faker import Faker
from faker.providers import DynamicProvider
from Donor_Faker import DonorFaker

class BloodSample:
    
    def __init__(self):
        self.faker = Faker()
        self.sample_id = self.faker.random_int(min=1, max=2147483647)
        
        resultProvider = DynamicProvider(
            provider_name="Results",
            elements=['+', '-']
        )
        self.faker.add_provider(resultProvider)
        self.results = self.faker.Results()
        



