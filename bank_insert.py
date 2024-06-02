from contact_number import NumberModifier
from Streets import Streets
from PostalCode import PostalCodes
from faker import Faker
from BloodBank_Faker import BloodBanks
import random
class BankInsert:
    def __init__(self) -> None:
       pass   
    
    @staticmethod
    def listappender(datalist):
      for i in range(1,101):
        obj=BloodBanks()
        data = obj.generate_bank()
        datalist.append((
            i,
            data['Telephone_Number'], 
            data['Name'], 
            data['Capacity'], 
            data['City'], 
            data['Street'], 
            data['Postal_Code']
        ))
      return datalist
    
    @staticmethod
    def insert(cursor,conn,datalist):
        insert_query_for_Donor = """
        INSERT INTO BloodBanks (License_id,Telephone_Number,Name,Capacity,City,Street,Postal_Code)
         VALUES (?, ?, ?, ?, ?, ?, ?)
         """
        for row in datalist:
           cursor.execute(insert_query_for_Donor, row)
           conn.commit()

        cursor.close()
        conn.close()