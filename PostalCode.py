from faker import Faker
from faker.providers import BaseProvider
import random

class PostalCodes(BaseProvider):
    def CityName(self):
        return random.choice([
            "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala",
            "Karachi", "Hyderabad", "Peshawar", "Mardan", "Abbottabad",
            "Swat", "Quetta", "Gwadar", "Gilgit", "Skardu", "Muzaffarabad", "Mirpur"
        ])
    
    def Postal_Codes(self, city_name):
        Codes = {
            "Lahore": [54000], #Lahore GPO
            "Faisalabad": [37250], #JARANWALA
            "Rawalpindi": [46020],# RAWALPINDI URDU BAZAR
            "Multan": [59000],#KADIRPUR RAWAN 
            "Gujranwala": [52132], #Wapda Town
            "Karachi": [74200], #Karachi GPO
            "Hyderabad": [65010], #DHARKI
            "Peshawar": [25000], #Peshawar
            "Mardan": [23350],  #Gujrat
            "Abbottabad": [22510], #PAK ORDINANCE FACTORIES HAVILIAN 
            "Swat": [19200],
            "Quetta": [86000],#Chaman
            "Gwadar": [91200],
            "Gilgit": [14100], #CHILAS (LSG)
            "Skardu": [16100], #SKARDU BAZAR
            "Muzaffarabad": [13250], #RAHIMKOT
            "Mirpur": [69260] #Nagar Parkar
        }
        return random.choice(Codes.get(city_name, []))