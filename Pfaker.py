from faker import Faker
from Donor_Faker import DonorFaker
from faker.providers import DynamicProvider


class patientFaker:
    
    def __init__(self):
        self.faker=Faker()
        fakerDonor=DonorFaker()
        self.donordata=fakerDonor.generate_donor()
        
        diseaseprovider=DynamicProvider(
            provider_name="disease",
            elements=['Thalassemia','Leukemia','Lymphoma','Multiple Myeloma','Hemophilia','Red Blood','Plasma','Platelets']
        )
        self.faker.add_provider(diseaseprovider)
       
    
    def insert(self):
        data= {}
        data['CNIC']= self.donordata['CNIC']
        data['Name']=self.donordata['Donor_Name']
        data['BG']=self.donordata['BloodType']
        data['disease']= self.faker.disease()
        return data

        
#test object
'''
patient=patientFaker()
print(patient.name)

'''
