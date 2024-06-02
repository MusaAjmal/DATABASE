from Pfaker import patientFaker

class patientinserter:

    def __init__(self) -> None:
        pass


    @staticmethod
    def appendlist(datalist):
        for i in range (1,201):
            patient= patientFaker()
            obj= patient.insert()
            datalist.append((
              obj['CNIC'],
              obj['Name'],
              obj['BG'],
              obj['disease']
                 
            ))
        return datalist
    @staticmethod
    def insert(cursor,conn,list):
        query = """insert into patients (CNIC,Name,Blood_Group,Disease_or_Emergency) 
        values (?,?,?,?)
        """
        for row in list:
            cursor.execute(query,row)
            cursor.commit()
        cursor.close()
        conn.close()
