'''
BloodUnit_id varchar(5), --pk
Blood_Group varchar(3) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
BloodCell_id tinyint, --fk
bloodbank_id int, --fk
backup_BloodBank_Id int, --fk
Donor_Id varchar(13) check (LEN(Donor_id) = 13 AND Donor_id LIKE '[1-9][0-9-]%' AND Donor_id NOT LIKE '%[^0-9-]%'),--fk
Storage_Date date default (getdate()),
Expiration_Date date,
unit_status varchar (15) check (unit_status in ('Available','Expired')),
'''
from faker import Faker
from faker.providers import DynamicProvider
from datetime import date,timedelta
from CellTypes import CellTypes

class BloodUnits:
    def __init__(self):
        self.faker=Faker()
        self.unit_id= self.faker.random_int(min=1111111111, max=2147483647)
        self.storage_date=date.today()
        cells=CellTypes()
        self.type= cells.generate_cell_type()
        if(self.type== 1):
            self.expiry_date=date.today() + timedelta(days=42)
        elif (self.type== 2):
            self.expiry_date=date.today() + timedelta(days=365)
        elif (self.type== 3):
            self.expiry_date=date.today() + timedelta(days=5)
        else:
            self.expiry_date= ''
            print("Error Type Not Identified")

        blood_group_provider = DynamicProvider(
            provider_name="bloodgroup",
            elements=['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']
        )
        self.faker.add_provider(blood_group_provider)
        self.blood_group=self.faker.bloodgroup()
        if(date.today == self.expiry_date):
             self.status='Expired'
        else:
            self.status='Available'


       

    def display_attributes(self):
        print(f"BloodUnit_id: {self.unit_id}")
        print(f"Blood_Group: {self.blood_group}")
        print(f"Storage_Date: {self.storage_date}")
        print(f"Expiration_Date: {self.expiry_date}")
        print(f"unit_status: {self.status}")
#Test Object
'''
units=BloodUnits()
units.display_attributes()
'''
