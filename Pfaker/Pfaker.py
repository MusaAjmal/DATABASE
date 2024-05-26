from faker import Faker
from DonorFaker.Donor_Faker import DonorFaker
from faker.providers import DynamicProvider


class patientFaker:
    
    def __init__(self):
        self.faker=Faker()
        fakerDonor=DonorFaker()
        donordata=fakerDonor.generate_donor()
        self.cnic=donordata['CNIC']
        self.name=donordata['Donor_Name']
        self.bg=donordata['BloodType']
        diseaseprovider=DynamicProvider(
            provider_name="disease",
            elements=['Thalassemia','Leukemia','Lymphoma','Multiple Myeloma','Hemophilia','Red Blood','Plasma','Platelets']
        )
        self.faker.add_provider(diseaseprovider)
        self.disease_emergency= self.faker.disease()

        

patient=patientFaker()
print(patient.disease_emergency)
