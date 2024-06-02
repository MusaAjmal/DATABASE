import pypyodbc as odbc
from datetime import datetime
from contact_number import NumberModifier
from Streets import Streets
from PostalCode import PostalCodes
from BloodBank_Faker import BloodBanks
from bank_insert import BankInsert
from patientAppender import patientinserter
from Pfaker import patientFaker
from TransfusionAppender import Transfusionappender
Driver_Name = 'SQL SERVER'
Server_Name = 'DESKTOP-24QJ69Q\SQLEXPRESS'
Database_Name = 'Project'

# ODBC connection string
connection_String = (
    f"Driver={{{Driver_Name}}};"
    f"Server={Server_Name};"
    f"Database={Database_Name};"
    f"Trusted_Connection=yes;"
)
conn = odbc.connect(connection_String)
print(conn)
cursor=conn.cursor()


list=[]
cnic=[]
unitid=[]
cnic=Transfusionappender.keyfetcherpatient(cursor)
unitid= Transfusionappender.keyfetcherunits(cursor)
list=Transfusionappender.appendlist(list,cnic,unitid)
Transfusionappender.insert(cursor,conn,list)