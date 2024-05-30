import pypyodbc as odbc
from contact_number import NumberModifier
from contactappender import ContactAppender
from Bloodsampleappender import SampleAppender
from BloodSample_for_Donor import BloodSample
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

# Connect to the database
conn = odbc.connect(connection_String)
print(conn)
cursor = conn.cursor()

list=[]
foreignkey_list = SampleAppender.getkeyDonor(cursor)
sample= BloodSample()
list=SampleAppender.generateSamples(list,sample,foreignkey_list)

SampleAppender.insertSample(cursor,conn,list)
