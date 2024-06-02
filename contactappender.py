from contact_number import NumberModifier
from faker import Faker
from donor_insert import DonorFaker

class ContactAppender:
    def __init__(self) -> None:
        pass    
    
    @staticmethod
    def getkeyDonor(cursor):
        query = """SELECT cnic FROM donors"""
        cursor.execute(query)
        res = [str(row[0]).strip(',') for row in cursor.fetchall()]
        return res
    
    @staticmethod
    def generateContact(datalist, contact, foreignkey_list):
        for i in range(1,2000):
            large_number = contact.generate_large_number()
            num_donors = len(foreignkey_list)
            modified_number = contact.set_first_digits(large_number)  # Number
            datalist.append((
                i,
                modified_number,
                foreignkey_list[i % num_donors]
            ))
        return datalist
    
    @staticmethod
    def insertContacts(cursor, conn, contactData):
        insert_query_for_Cell_Number = """
        INSERT INTO Cell_Number (CellNo_Id, Number, Donor_CNIC)
        VALUES (?, ?, ?)
        """
        for row in contactData:
            cursor.execute(insert_query_for_Cell_Number, row)
            conn.commit()
        cursor.close()
        conn.close()
