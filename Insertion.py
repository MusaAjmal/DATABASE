import pypyodbc as odbc
from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime
from Donor_Faker import DonorFaker
from contact_number import NumberModifier

Driver_Name = 'SQL SERVER'
Server_Name = 'MUSA\SQLEXPRESS'
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

######### DONOR INSERTION ###########

Donor_data=[]  # data insertion list for donor entity
Cniclist_Donor=[]

donorfaker=DonorFaker() # object for donor entity 
def Donor_Generator():

    for i in range (1, 2000):
        data=donorfaker.generate_donor()
        Cniclist_Donor.append((data['CNIC']))
        Donor_data.append((
        data['CNIC'],
        data['Donor_Name'],
        data['Date_Of_Birth'],
        data['Province'],
        data['City'],
        data['Eligible'],
        data['BloodType']

        ))
    return Donor_data
Donor_data= Donor_Generator() ## appending data to list
f1= Faker()  # faker to randomize foreign key (donor)
cnicp=DynamicProvider(
    provider_name='cnic',
    elements=Cniclist_Donor
)
f1.add_provider(cnicp)


def insertDonors():
    insert_query_for_Donor = """
    INSERT INTO Donors (CNIC, Donor_Name, Date_Of_Birth, Province, City, Eligible, BloodType)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    for row in Donor_data:
        cursor.execute(insert_query_for_Donor, row)
        conn.commit()

   # cursor.close()
    #conn.close()

#insertDonors() Dangerous
###########   Contact Number Insertion #################
contactData=[]
number_modifier = NumberModifier(3)

def ContactGenerator():
    for i in range(1,30000):
        large_number = number_modifier.generate_large_number()
        num_donors = len(Cniclist_Donor)
        modified_number = number_modifier.set_first_digits(large_number) ##Number
        contactData.append((
            i,
            modified_number,
            Cniclist_Donor[i % num_donors]

        ))
    return contactData
contactData= ContactGenerator()


def insertContacts():

    insert_query_for_Cell_Number = """
    INSERT INTO Cell_Number (CellNo_Id, Number, Donor_CNIC)
    VALUES (?, ?, ?)
    """
    for row in contactData:
        cursor.execute(insert_query_for_Cell_Number,row)
        conn.commit()
    cursor.close()
    conn.close()
#insertContacts() dangerous!!!
#####################################