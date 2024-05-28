from faker import Faker
from faker.providers import DynamicProvider
from contact_number import NumberModifier
from Streets import Streets
from faker.providers import BaseProvider
from PostalCode import PostalCodes

class BloodBanks:
    def __init__(self):
        self.faker = Faker()
        self.license_id = self.faker.random_int(min=1111111111, max=2147483647)
        number_modifier = NumberModifier(3)
        large_number = number_modifier.generate_large_number()
        self.number = number_modifier.set_first_digits(large_number)
        hospital_name_provider = DynamicProvider(
            provider_name="hospital_name",
            elements=[
                "Shifa International Hospital",
                "Aga Khan University Hospital",
                "Liaquat National Hospital",
                "Jinnah Postgraduate Medical Centre",
                "Lahore General Hospital",
                "Faisal Hospital",
                "Rawalpindi General Hospital",
                "Nishtar Medical University Hospital",
                "Khyber Teaching Hospital",
                "Bolan Medical Complex Hospital",
                "Quetta Civil Hospital",
                "Gilgit Baltistan Hospital",
                "Muzaffarabad District Headquarters Hospital",
                "Mirpur Azad Kashmir Hospital",
                "Bahawal Victoria Hospital",
                "Jinnah Hospital Lahore",
                "Dow University Hospital",
                "Ziauddin Hospital",
                "Indus Hospital Network",
                "Shaukat Khanum Memorial Hospital",
                "Aga Khan Development Network Hospitals",
                "Hayatabad Medical Complex",
                "Khyber Teaching Hospital",
                "Ayub Teaching Hospital",
                "Benazir Bhutto Hospital",
                "Larkana Civil Hospital",
                "Nawabshah Medical College Hospital",
                "Ghulam Muhammad Mahar Medical College Hospital",
                "Liaquat University Hospital",
                "Chandka Medical College Hospital"
            ]
        )
        self.faker.add_provider(hospital_name_provider)
        self.capacity = 0
        city_provider = DynamicProvider(
            provider_name="Cities",
            elements=["Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala",
                       "Karachi", "Hyderabad",
                       "Peshawar", "Mardan", "Abbottabad", "Swat",
                       "Quetta", "Gwadar",
                       "Gilgit", "Skardu",
                       "Muzaffarabad", "Mirpur"]
        )
        self.faker.add_provider(city_provider)
        streets_provider = Streets(BaseProvider)
        self.faker.add_provider(streets_provider)
        postal_code_provider = PostalCodes(BaseProvider)
        self.faker.add_provider(postal_code_provider)

    def generate_bank(self):
        bank_data = {}
        bank_data['License_id'] = self.license_id
        bank_data['Telephone_Number'] = self.number
        bank_data['Name'] = self.faker.hospital_name()
        bank_data['Capacity'] = 0
        bank_data['City'] = self.faker.Cities()
        bank_data['Street'] = self.faker.street_address(bank_data['City'])
        bank_data['Postal_Code'] = self.faker.Postal_Codes(bank_data['City'])
        return bank_data
    
    def print_bank_data(self):
        bank_data = self.generate_bank()
        for key, value in bank_data.items():
            print(f"{key}: {value}")

#Test Object
'''banks = BloodBanks()
bank_data = banks.generate_bank()
print(bank_data['Name'])'''
