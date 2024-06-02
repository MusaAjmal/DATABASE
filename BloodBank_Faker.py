from faker import Faker
from faker.providers import DynamicProvider
from contact_number import NumberModifier
from Streets import Streets
from faker.providers import BaseProvider
from PostalCode import PostalCodes

class BloodBanks:
    def __init__(self):
        self.faker = Faker()
       # self.licenseid=self.faker.unique.random_int(min=1000, max=999)
        number_modifier = NumberModifier(3)
        large_number = number_modifier.generate_large_number()
        self.number = number_modifier.set_first_digits(large_number)
        hospital_name_provider = DynamicProvider(
            provider_name="hospital_name",
            elements=[
                      "Blood Unit DHQ",
                      "District Blood Transfusion Unit",
                      "Regional Blood Center",
                      "Blood Bank Allied Hospital",
                      "Blood Bank FIC",
                      "Blood Bank THQ Hospital",
                      "Blood Bank Services Hospital",
                      "Blood Bank PIC",
                      "INMOL Blood Bank",
                      "Blood Bank Sheikh Zayed Hospital",
                      "Blook Bank Children Hospital",
                      "Mayo Hospital Blood Bank",
                      "Blood Unit Kot Khawaja Saeed",
                      "Blood Bank Lahore General Hospital",
                      "Blood Bank Jinnah Hospital",
                      "Blood Bank Ghulab Davi Hospital",
                      "Blood Bank Sir Ganga Ram Hospital",
                      "Blood Bank Nawaz Sharif Hospital",
                      "Blood Bank Lady Aitchison Hospital",
                      "Blood Bank Lady Willingdon Hospital",
                      "Blood Bank IBTS",
                      "Nawaz Sharif Social Hospital",
                      "Avicenna Medical College Blood Bank",
                      "Blood Transfusion Unit DHQ Hospital",
                      "Regional Blood Center",
                      "Nishter Hospital Blood Bank",
                      "Blood Bank SZMC",
                      "District Blood Transfusion Office",
                      "Blood Unit Holy Family Hospital",
                      "Blood Unit Banazir BhuttoHospital",
                      "Blood Bank RIC",
                      "Tehsil Blood Unit",
                      "Blood Bank Sundus Foundation",
                      "Noor-ul-Ain Dyra Tal Khidmat Alinsaniyah",
                      "Madina Teaching Hospital Blood Bank",
                      "Blood Bank Independent University Hospital",
                      "Aziz Fatimah Hospital",
                      "Zahid Lab Chattha Hospital",
                      "Blood Bank Al-Raee Hospital",
                      "Blood Bank Chughtais Lahore Lab",
                      "Nabeel Blood Bank Niaz Memorial Hospital",
                      "Shoukat Khanum Memorial Trust",
                      "SUNDUS Foundation Blood Bank",
                      "Mid City Hospital Blood Bank",
                      "Farooq Hospital Blood Bank",
                      "Amina Bashir Memorial Trust Hospital",
                      "Sharif Medical City Hospital",
                      "Omer Hospital Laboratories",
                      "Shalimar Hospital Laboratories",
                      "Ghurki Trist Teaching Hospital",
                      "Chughtais Lahore Lab",
                      "Chughtais Lahore Lab",
                      "Surgimid Hospital Laboratory",
                      "Lahore Blood Bank",
                      "Al-Khidmat Blood BAnk",
                      "Blood Transfusion Services",
                      "AMC Excel Lab Blood Bank",
                      "Blood Bank Company",
                      "Iqra Blood Bank",
                      "Akhtar Saeed Trust Blood Bank",
                      "Farooq Hospital Blood Bank",
                      "Blood Bank Hameed Latif Hospital",
                      "Bahria Town Hospital",
                      "FMH Clinical Lab Blood Bank",
                      "Pathology Lab Wapda Complex",
                      "Cavalary Hospital Blood Bank",
                      "Doctors Hospital & Medical Centre",
                      "Adil Hosputal DHA Blood Bank",
                      "University of Lahore Blood Bank",
                      "Muhammad Shahbaz Sharif Hospital",
                      "Excel Lab Blood Bank SMH Lahore",
                      "Masood Hospital Laboratory",
                      "Blood Unit Punjab Health Management Company",
                      "Blood Bank Ch. Muhammad Akram & Research Hospital",
                      "Bahria International Hospital Blood Bank",
                      "Blood Bank Hijaz Hospital",
                      "Blood Bank Family Hospital"
                                  ]
        )
        self.faker.add_provider(hospital_name_provider)
        self.Capacity = self.faker.unique.random_int(min=300,max=1000)
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
        #bank_data['License_id'] = self.licenseid
        bank_data['Telephone_Number'] = self.number
        bank_data['Name'] = self.faker.hospital_name()
        bank_data['Capacity'] = self.Capacity
        bank_data['City'] = self.faker.Cities()
        bank_data['Street'] = self.faker.street_address(bank_data['City'])
        bank_data['Postal_Code'] = self.faker.Postal_Codes(bank_data['City'])
        return bank_data
    
    def print_bank_data(self):
        bank_data = self.generate_bank()
        for key, value in bank_data.items():
            print(f"{key}: {value}")

#Test Object
