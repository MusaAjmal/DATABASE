from faker import Faker

class NumberModifier:
    def __init__(self, predefined_digits):
        self.predefined_digits = str(predefined_digits)
        self.faker = Faker()
        
    def set_first_digits(self, large_number):
        large_number_str = str(large_number)
        modified_number_str = self.predefined_digits + large_number_str[len(self.predefined_digits):]
        modified_number = int(modified_number_str)
        return modified_number

    def generate_large_number(self, min_value=10000000000, max_value=99999999999):
        return self.faker.unique.random_int(min=min_value, max=max_value)
    
#Test Object
'''number_modifier = NumberModifier(3)
large_number = number_modifier.generate_large_number()
modified_number = number_modifier.set_first_digits(large_number)
print(modified_number)'''
