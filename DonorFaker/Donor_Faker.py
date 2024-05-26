from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime
from Donor_or_Patient_Names import PakistaniNamesGenerator
from Provinces import ProvinceProvider
from faker.providers import BaseProvider

class Donor_Faker:
    '''CNIC varchar(13) CHECK (LEN(CNIC) = 13 AND CNIC LIKE '[1-9][0-9-]%' AND CNIC NOT LIKE '%[^0-9-]%'),--pk
Donor_Name varchar(50),
Date_Of_Birth date,
Province varchar(50),
City varchar(50),
Eligible varchar(3) check (Eligible in ('Yes','No')),
BloodType varchar(5) check(BloodType in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
constraint pk_donor_id primary key (CNIC)'''
boys_url = "https://pakistaninames.wordpress.com/pakistani-boys-names/"
girls_url = "https://pakistaninames.wordpress.com/pakistani-girls-names/"
faker_donor= Faker()
#cnic= str(faker_donor.unique.random_int(min=11111111111,max=99999999999))
nameprovider= DynamicProvider(
    provider_name="Rname",
    elements= PakistaniNamesGenerator.generate_full_names()
)
faker_donor.add_provider(nameprovider)
#name=faker_donor.Rname()
donor_max_age = datetime(2006, 1, 1)
donor_min_age = datetime(1996, 1, 1)
#donor_DOB = faker_donor.date_time_between(start_date=donor_min_age, end_date=donor_max_age).strftime("%Y-%m-%d")
provinceprovider =DynamicProvider(
   provider_name="provincename",
   elements= ['Punjab','Sindh','Balochistan','Khyber Phakhtunkhwa','Gilgit Baltistan','Azad Kashmir']
)
faker_donor.add_provider(provinceprovider)
#donor_province= faker_donor.provincename()
pprovider= ProvinceProvider(BaseProvider) #class for province-> city probelm
faker_donor.add_provider(pprovider)
#cityname=faker_donor.cityname(faker_donor.provincename())
eligibilityprovider= DynamicProvider(
    provider_name="iseligible",
    elements=['Yes','No']
)
faker_donor.add_provider(eligibilityprovider)
#elig=faker_donor.iseligible()
bloodgroupprovider= DynamicProvider(
    provider_name="bloodgroup",
    elements=['A+','O+','B+','AB+','A-','O-','B-','AB-']
)
faker_donor.add_provider(bloodgroupprovider)
#bg=faker_donor.bloodgroup()










