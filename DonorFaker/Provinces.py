from faker import Faker
from faker.providers import BaseProvider
import random

class ProvinceProvider(BaseProvider):
    def provincename(self):
        return random.choice(['Punjab', 'Sindh', 'Balochistan', 'Khyber Pakhtunkhwa', 'Gilgit Baltistan', 'Azad Kashmir'])
    
    def cityname(self, province_name):
        cities = {
            "Punjab": ["Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala", "Sialkot", "Bahawalpur", "Gujrat", "Sargodha", "Sheikhupura"],
            "Sindh": ["Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah", "Mirpur Khas", "Jacobabad", "Shikarpur", "Dadu", "Tando Adam"],
            "Khyber Pakhtunkhwa": ["Peshawar", "Mardan", "Abbottabad", "Swat", "Charsadda", "Nowshera", "Kohat", "Haripur", "Dera Ismail Khan", "Mansehra"],
            "Balochistan": ["Quetta", "Gwadar", "Turbat", "Khuzdar", "Chaman", "Sibi", "Zhob", "Nushki", "Kalat", "Pasni"],
            "Gilgit Baltistan": ["Gilgit", "Skardu", "Chilas", "Ghizer", "Astore", "Hunza", "Khaplu", "Shigar", "Gahkuch", "Diamer"],
            "Azad Kashmir": ["Muzaffarabad", "Mirpur", "Bhimber", "Kotli", "Rawalakot", "Bagh", "Hattian", "Neelum", "Sudhanoti", "Haveli"]
        }
        return random.choice(cities.get(province_name, []))



