from Transfusions import Transfusions

class Transfusionappender:

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def keyfetcherpatient(cursor):
        query = """select CNIC FROM Patients"""
        cursor.execute(query)
        res = [str(row[0]).strip(',') for row in cursor.fetchall()]
        return res
    
    @staticmethod
    def keyfetcherunits(cursor):
        query = """select BloodUnit_id FROM BloodUnits"""
        cursor.execute(query)
        res = [str(row[0]).strip(',') for row in cursor.fetchall()]
        return res

    @staticmethod
    def appendlist(datalist,fetched1,fetched2):
        l=len(fetched1)
        s= len(fetched2)
        for i in range(1,1000):
            transfusions= Transfusions()
            temp= transfusions.generate()
            datalist.append((
             temp['id'],
             fetched1[ i % l],
             temp['startdate'],
             fetched2[ i % s]
            ))
        return datalist
    @staticmethod
    def insert(cursor,conn,datalist):
        query="""
               insert into Transfusions(Transfusion_id,patient_id,Transfusion_Date,bloodunit_id)
               values(?,?,?,?)
                """
        for row in datalist:
            cursor.execute(query,row)
            cursor.commit()
        cursor.close()
        conn.close()    

