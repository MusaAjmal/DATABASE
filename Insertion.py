import pypyodbc as odbc
from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime
from Donor_Faker import DonorFaker
from contact_number import NumberModifier
from BloodSample_for_Donor import BloodSample

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
Cniclist_Donor=[] #saving foreign key for donor

donorfaker=DonorFaker() # object for donor entity 
def Donor_Generator():

    for i in range (1, 2000):
        data=donorfaker.generate_donor()
        
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
def insertDonors():
    insert_query_for_Donor = """
    INSERT INTO Donors (CNIC, Donor_Name, Date_Of_Birth, Province, City, Eligible, BloodType)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    for row in Donor_data:
        cursor.execute(insert_query_for_Donor, row)
        conn.commit()

    #cursor.close()
    #conn.close()

#insertDonors()  ##DANGER
def getkeyDonor():
    query="""select cnic from donors"""
    cursor.execute(query)
    res = [str(row[0]).strip(',') for row in cursor.fetchall()]
    return res

Cniclist_Donor=getkeyDonor() #DANGER WEWOWEWO

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
#insertContacts()  ##DANGER WEWOWEWO
################Blood SAMPLE#####################
SampleList=[]
num_donors=len(Cniclist_Donor)
def sampleGenerator():
    for i in range(1,50000):
        
        sample=BloodSample()
        SampleList.append((sample.sample_id,Cniclist_Donor[i % num_donors],sample.results))
    return SampleList

SampleList= sampleGenerator()
for wo in SampleList:
    print(wo)

def sampleinsert():
    query="""insert into Blood_Samples (Sample_id,Donor_id,Result) values (?,?,?)"""
    for row in SampleList:
        cursor.execute(query,row)
        conn.commit()
    cursor.close()
    conn.close()

#sampleinsert() #DANGER WEWOWEWO