from faker import Faker
from Donor_Faker import DonorFaker

class NumberModifier:
    def __init__(self, predefined_digits):
        self.predefined_digits = predefined_digits
        self.faker = Faker()
        instance=DonorFaker()
        donor=instance.generate_donor()
        self.cnic=donor['CNIC']

    def set_first_three_digits(self, large_number):
        predefined_str = str(self.predefined_digits)
        large_number_str = str(large_number)

        
        modified_number_str = predefined_str + large_number_str[1:]

        modified_number = int(modified_number_str)
        return modified_number

    def generate_large_number(self, min_value=11111111111, max_value=99999999999):
        return self.faker.random_int(min=min_value, max=max_value)
    
