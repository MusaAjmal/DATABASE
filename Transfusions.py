'''
Transfusion_id int, --pk
patient_id varchar(13) check (LEN(patient_id) = 13 AND patient_id LIKE '[1-9][0-9-]%' AND patient_id NOT LIKE '%[^0-9-]%'),--fk
Transfusion_Date date default (getdate()),
BloodUnit_id varchar(5),
backup_BloodUnit_id varchar(5)
'''
from faker import Faker
from datetime import date

class Transfusions:
    def __init__(self):
        self.faker=Faker()
        self.transfusion_id=self.faker.random_int(min=1111111111, max=2147483647)
        self.transfusion_date=date.today()

#Test Object
'''
t= Transfusions()
print(t.transfusion_id)
print(t.transfusion_date)
'''
