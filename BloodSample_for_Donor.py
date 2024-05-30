from faker import Faker
from faker.providers import DynamicProvider

class BloodSample:
    def __init__(self):
        self.faker = Faker()
        self._add_providers()
        resultProvider = DynamicProvider(
            provider_name="Results",
            elements=['+', '-']
        )
        self.faker.add_provider(resultProvider)
        
    def assign_values(self):
        self.sample_id = self.faker.random_int(min=1, max=2147483647)
        self.results = self.faker.Results()
