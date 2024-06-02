from faker import Faker
from faker.providers import BaseProvider
import random

class Streets(BaseProvider):
    def CityName(self):
        return random.choice([
            "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala",
            "Karachi", "Hyderabad", "Peshawar", "Mardan", "Abbottabad",
            "Swat", "Quetta", "Gwadar", "Gilgit", "Skardu", "Muzaffarabad", "Mirpur"
        ])
      
    def street_address(self, city_name):
        streets = {
            "Lahore": [
                "7A Block R3, Johar Town",
                "Neela Gumbad Anarkali, Mall Road",
                "Jail Road, G.O.R.-I",
                "Usmani Road, Faisal Town",
                "Shadman Rd, Ichhra"
            ],
            "Faisalabad": [
                "Jail Road",
                "West Canal Road",
                "Satiana Road",
                "Jail Road",
                "D-Type Colony"
            ],
            "Rawalpindi": [
                "Murree Road",
                "Tipu Road, Satellite Town",
                "Rawal Road",
                "Raja Bazaar",
                "Rawal Road"
            ],
            "Multan": [
                "Nishtar Road",
                "Al Rahim Colony, Khanewal Road",
                "Northern Bypass",
                "Abdali Road",
                "Khanewal Road"
            ],
            "Gujranwala": [
                "Sialkot Road",
                "Hospital Road",
                "Alipur Chatha Road",
                "Gondlanwala Road",
                "G.T. Road"
            ],
            "Karachi": [
                "Stadium Road",
                "Rafiqui Shaheed Road",
                "Baba-e-Urdu Road",
                "National Stadium Road",
                "St-1, Block 3, Clifton"
            ],
            "Hyderabad": [
                "Thandi Sarak",
                "Jamshoro Road",
                "Auto Bhan Road",
                "Station Road",
                "Hala Road"
            ],
            "Peshawar": [
                "University Road",
                "Soekarno Road",
                "Hayatabad Phase 4",
                "5-B/2, Phase-V, Hayatabad",
                "Sector A-3, Phase-V, Hayatabad"
            ],
            "Mardan": [
                "Nowshera Road",
                "Nowshera Road",
                "Ring Road",
                "Bank Road",
                "Bacha Khan Chowk"
            ],
            "Abbottabad": [
                "Karakoram Highway",
                "Mandian",
                "PMA Kakul Road",
                "Main Mansehra Road",
                "Mandian"
            ],
            "Swat": [
                "Mingora",
                "Saidu Sharif",
                "Mingora",
                "Mingora",
                "Mingora"
            ],
            "Quetta": [
                "Brewery Road",
                "Jinnah Road",
                "Brewery Road",
                "McConghy Road",
                "Chiltan Road"
            ],
            "Gwadar": [
                "Jinnah Avenue",
                "Airport Road",
                "Gwadar Port Area",
                "Sarwan",
                "PNS Akram"
            ],
            "Gilgit": [
                "Airport Road",
                "Jutial",
                "Jutial",
                "Sakwar",
                "Gilgit-Skardu Road"
            ],
            "Skardu": [
                "Alamdar Road",
                "Haji Gham",
                "New Bazaar",
                "Sadpara Road",
                "Chowk Yadgar"
            ],
            "Muzaffarabad": [
                "CMH Road",
                "CMH Road",
                "CMH Road",
                "Domel",
                "Upper Chattar"
            ],
            "Mirpur": [
                "Mirpur",
                "Jari Kass",
                "Allama Iqbal Road",
                "Mirpur",
                "Defence Road"
            ]
            }
        return random.choice(streets.get(city_name, []))
