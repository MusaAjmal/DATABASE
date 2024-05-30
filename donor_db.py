import pypyodbc as odbc
from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime
from Donor_Faker import DonorFaker
from contact_number import NumberModifier
from BloodSample_for_Donor import BloodSample
from donor_insert import Donor_insert

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
cursor=conn.cursor()

donor=DonorFaker()

list= []
list= Donor_insert.GenerateDonor(donor,list)
Donor_insert.insertDonors(cursor,conn,list)