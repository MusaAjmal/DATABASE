from BloodSample_for_Donor import BloodSample

class SampleAppender:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def getkeyDonor(cursor):
        query = """SELECT cnic FROM donors"""
        cursor.execute(query)
        res = [str(row[0]).strip(',') for row in cursor.fetchall()]
        return res
    
    @staticmethod
    def generateSamples(datalist, obj, foreignkey_list):
        count = len(foreignkey_list)
        for i in range(1,1500):
            temp = obj.insert()
            datalist.append((
                temp["id"],
                foreignkey_list[i % count],
                temp["results"]
            ))
        return datalist
    
    @staticmethod
    def insertSample(cursor, conn, datalist):
        query = """INSERT INTO Blood_Samples (Sample_id, Donor_id, Result) VALUES (?, ?, ?)"""
        for row in datalist:
            cursor.execute(query, row)
            conn.commit()
        cursor.close()
        conn.close()
