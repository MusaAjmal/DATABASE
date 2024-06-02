from BloodUnits import BloodUnits

class bloodunitappender:
    def __init__(self) -> None:
        pass
    @staticmethod

    def fetchkeybloodbanks(cursor):
        query = """ select License_id FROM BloodBanks"""
        cursor.execute(query)
        res = [str(row[0]).strip(',') for row in cursor.fetchall()]
        return res
    @staticmethod
    def fetchkeydonors(cursor):
        query = """select CNIC FROM Donors"""
        cursor.execute(query)
        res = [str(row[0]).strip(',') for row in cursor.fetchall()]
        return res
    @staticmethod
    def appendlist(datalist,fetched1,fetched2):
        c=len(fetched1)
        d= len(fetched2)
        for i in range(1,1000):
            unit=BloodUnits()
            obj=unit.insert()
            datalist.append((
               obj['id'],
               obj['bg'],
               obj['type'],
               fetched1[i % c],
               fetched2[i % d],
               obj['storagedate'],
               obj['expirydate'],
               obj['status']

            ))
        return datalist
    @staticmethod
    def insert(cursor,conn,datalist):
        query = """ insert into BloodUnits(BloodUnit_id,Blood_Group,BloodCell_id,bloodbank_id,Donor_id,Storage_Date,Expiration_Date,unit_status)
                 values(?,?,?,?,?,?,?,?) """
        for row in datalist:
            cursor.execute(query,row)
            cursor.commit()
        cursor.close()
        conn.close()
        
