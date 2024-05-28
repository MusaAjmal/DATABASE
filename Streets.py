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
                "Shaukat Khanum Memorial Cancer Hospital & Research Centre, 7A Block R3, Johar Town",
                "Mayo Hospital, Neela Gumbad Anarkali, Mall Road",
                "Services Hospital, Jail Road, G.O.R.-I",
                "Jinnah Hospital, Usmani Road, Faisal Town",
                "Fatima Memorial Hospital, Shadman Rd, Ichhra"
            ],
            "Faisalabad": [
                "Allied Hospital, Jail Road",
                "Faisal Hospital, West Canal Road",
                "National Hospital, Satiana Road",
                "PINUM Cancer Hospital, Jail Road",
                "Hilal-e-Ahmar Hospital, D-Type Colony"
            ],
            "Rawalpindi": [
                "Benazir Bhutto Hospital, Murree Road",
                "Holy Family Hospital, Tipu Road, Satellite Town",
                "Rawalpindi Institute of Cardiology, Rawal Road",
                "District Headquarters Hospital, Raja Bazaar",
                "Bilal Hospital, Rawal Road"
            ],
            "Multan": [
                "Nishtar Hospital, Nishtar Road",
                "Ibn-e-Siena Hospital & Research Institute, Al Rahim Colony, Khanewal Road",
                "Bakhtawar Amin Memorial Hospital, Northern Bypass",
                "Fatima Medical Centre, Abdali Road",
                "Mukhtar A. Sheikh Hospital, Khanewal Road"
            ],
            "Gujranwala": [
                "DHQ Hospital, Sialkot Road",
                "Civil Hospital, Hospital Road",
                "Gujranwala Medical College Teaching Hospital, Alipur Chatha Road",
                "Life Care Hospital, Gondlanwala Road",
                "Ravi Hospital, G.T. Road"
            ],
            "Karachi": [
                "Aga Khan University Hospital, Stadium Road",
                "Jinnah Postgraduate Medical Centre, Rafiqui Shaheed Road",
                "Civil Hospital, Baba-e-Urdu Road",
                "Liaquat National Hospital, National Stadium Road",
                "South City Hospital, St-1, Block 3, Clifton"
            ],
            "Hyderabad": [
                "Civil Hospital, Thandi Sarak",
                "Liaquat University Hospital, Jamshoro Road",
                "Red Crescent General Hospital, Auto Bhan Road",
                "Rajputana Hospital, Station Road",
                "ISRA University Hospital, Hala Road"
            ],
            "Peshawar": [
                "Khyber Teaching Hospital, University Road",
                "Lady Reading Hospital, Soekarno Road",
                "Hayatabad Medical Complex, Hayatabad Phase 4",
                "Rehman Medical Institute, 5-B/2, Phase-V, Hayatabad",
                "North West General Hospital, Sector A-3, Phase-V, Hayatabad"
            ],
            "Mardan": [
                "Mardan Medical Complex, Nowshera Road",
                "MMC General Hospital, Nowshera Road",
                "Qazi Hussain Ahmad Medical Complex, Ring Road",
                "Mardan City Hospital, Bank Road",
                "DHQ Teaching Hospital, Bacha Khan Chowk"
            ],
            "Abbottabad": [
                "Ayub Teaching Hospital, Karakoram Highway",
                "Abbottabad International Medical College Hospital, Mandian",
                "Combined Military Hospital (CMH), PMA Kakul Road",
                "Rehmat Memorial Hospital, Main Mansehra Road",
                "Women & Children Hospital, Mandian"
            ],
            "Swat": [
                "Saidu Teaching Hospital, Mingora",
                "Saidu Group of Teaching Hospitals, Saidu Sharif",
                "Zanana Hospital, Mingora",
                "Mingora Eye Hospital, Mingora",
                "Dr. Khan Diagnostic Centre, Mingora"
            ],
            "Quetta": [
                "Bolan Medical Complex Hospital, Brewery Road",
                "Civil Hospital Quetta, Jinnah Road",
                "Fatima Jinnah General & Chest Hospital, Brewery Road",
                "Helper Eye Hospital, McConghy Road",
                "Combined Military Hospital (CMH), Chiltan Road"
            ],
            "Gwadar": [
                "Gwadar Development Authority Hospital, Jinnah Avenue",
                "DHQ Hospital Gwadar, Airport Road",
                "Pak-China Friendship Hospital, Gwadar Port Area",
                "Basic Health Unit, Sarwan",
                "Navy Hospital, PNS Akram"
            ],
            "Gilgit": [
                "DHQ Hospital Gilgit, Airport Road",
                "CMH Gilgit, Jutial",
                "City Hospital, Jutial",
                "Women & Children Hospital, Sakwar",
                "Gilgit Eye Hospital, Gilgit-Skardu Road"
            ],
            "Skardu": [
                "DHQ Hospital Skardu, Alamdar Road",
                "CMH Skardu, Haji Gham",
                "Skardu City Hospital, New Bazaar",
                "M.H. Pura Hospital, Sadpara Road",
                "Women & Children Hospital, Chowk Yadgar"
            ],
            "Muzaffarabad": [
                "Abbas Institute of Medical Sciences, CMH Road",
                "Sheikh Khalifa Bin Zayed Al Nahyan Hospital, CMH Road",
                "Combined Military Hospital (CMH), CMH Road",
                "District Headquarters Hospital, Domel",
                "CMH Muzaffarabad, Upper Chattar"
            ],
            "Mirpur": [
                "Divisional Headquarters Hospital, Mirpur",
                "Mirpur Institute of Medical Sciences (MIMS), Jari Kass",
                "New City Hospital, Allama Iqbal Road",
                "Benazir Bhutto Shaheed Hospital, Mirpur",
                "CMH Mirpur, Defence Road"
            ]
        }
        return random.choice(streets.get(city_name, []))
