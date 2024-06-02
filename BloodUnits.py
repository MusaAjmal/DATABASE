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
import random
import string
from datetime import date,timedelta
from CellTypes import CellTypes

class BloodUnits:
    def __init__(self):
        self.faker=Faker()

        blood_group_provider = DynamicProvider(
            provider_name="bloodgroup",
            elements=['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']
        )
        self.faker.add_provider(blood_group_provider)
        

    def generate_alphanumeric_string(self,length=5, current_string=''):
        characters = string.ascii_uppercase + string.digits
        if len(current_string) == length:
            return current_string
        return self.generate_alphanumeric_string(length, current_string + random.choice(characters))
       
    def insert(self):
        data= {}
        
        data['id']=self.generate_alphanumeric_string(5,'')
        curr=date.today()
        data['storagedate']=curr.strftime("%Y-%m-%d")
        cells=CellTypes()
        #self.type= cells.generate_cell_type()
        data['type']=cells.generate_cell_type()
        if(data['type']== 1):
            exp=date.today() + timedelta(days=42)
            data['expirydate']=exp.strftime("%Y-%m-%d")
        elif (data['type']== 2):
            exp=date.today() + timedelta(days=365)
            data['expirydate']=exp.strftime("%Y-%m-%d")
        elif (data['type']== 3):
            exp=date.today() + timedelta(days=5)
            data['expirydate']=exp.strftime("%Y-%m-%d")
            
        else:
            data['expirydate']= ''
            print("Error Type Not Identified")
        data['bg']=self.faker.bloodgroup()
        if(date.today == data['expirydate']):
             data['status']='Expired'
        else:
            data['status']='Available'
        return data
    

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
