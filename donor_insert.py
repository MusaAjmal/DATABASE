from Donor_Faker import DonorFaker

class Donor_insert:
    def __init__(self) -> None:
        pass

    @staticmethod
    def GenerateDonor(donor_object,datalist):
        for i in range (1,1000):
            temp= donor_object.generate_donor()
            datalist.append((
                temp['CNIC'],
                temp['Donor_Name'],
                temp['Date_Of_Birth'],
                temp['Province'],
                temp['City'],
                temp['Eligible'],
                temp['BloodType']
            ))
        return datalist
    @staticmethod
    def insertDonors(cursor,conn,list):
        insert_query_for_Donor = """
        INSERT INTO Donors (CNIC, Donor_Name, Date_Of_Birth, Province, City, Eligible, BloodType)
         VALUES (?, ?, ?, ?, ?, ?, ?)
         """
        for row in list:
           cursor.execute(insert_query_for_Donor, row)
           conn.commit()

        cursor.close()
        conn.close()

        
            

