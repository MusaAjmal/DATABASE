from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime
from Donor_or_Patient_Names import PakistaniNamesGenerator
from Provinces import ProvinceProvider
from faker.providers import BaseProvider

class DonorFaker:
    def __init__(self):
        self.faker_donor = Faker()
        
        # Adding Name Provider
        name_provider = DynamicProvider(
            provider_name="Rname",
            elements=PakistaniNamesGenerator.generate_full_names()
        )
        self.faker_donor.add_provider(name_provider)
        
        # Adding Province Provider
        province_provider = DynamicProvider(
            provider_name="provincename",
            elements=['Punjab', 'Sindh', 'Balochistan', 'Khyber Phakhtunkhwa', 'Gilgit Baltistan', 'Azad Kashmir']
        )
        self.faker_donor.add_provider(province_provider)
        
        # Adding City Provider
        city_provider = ProvinceProvider(BaseProvider)
        self.faker_donor.add_provider(city_provider)
        
        # Adding Eligibility Provider
        eligibility_provider = DynamicProvider(
            provider_name="iseligible",
            elements=['Yes', 'No']
        )
        self.faker_donor.add_provider(eligibility_provider)
        
        # Adding Blood Group Provider
        blood_group_provider = DynamicProvider(
            provider_name="bloodgroup",
            elements=['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']
        )
        self.faker_donor.add_provider(blood_group_provider)
        
        # Defining date range for Donor's Date of Birth
        self.donor_max_age = datetime(2006, 1, 1)
        self.donor_min_age = datetime(1996, 1, 1)

    def generate_donor(self):
        donor_data = {}
        
        # Generating CNIC
        donor_data['CNIC'] = str(self.faker_donor.unique.random_int(min=1111111111111, max=9999999999999))
        
        # Generating Donor Name
        donor_data['Donor_Name'] = self.faker_donor.Rname()
        
        # Generating Date of Birth
        donor_data['Date_Of_Birth'] = self.faker_donor.date_time_between(start_date=self.donor_min_age, end_date=self.donor_max_age).strftime("%Y-%m-%d")
        
        # Generating Province
        donor_data['Province'] = self.faker_donor.provincename()
        
        # Generating City
        donor_data['City'] = self.faker_donor.cityname(donor_data['Province'])
        
        # Generating Eligibility
        donor_data['Eligible'] = self.faker_donor.iseligible()
        
        # Generating Blood Type
        donor_data['BloodType'] = self.faker_donor.bloodgroup()
        
        return donor_data


