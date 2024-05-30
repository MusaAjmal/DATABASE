import pypyodbc as odbc
from contact_number import NumberModifier
from contactappender import ContactAppender

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

# List to store data
datalist = []

# Create an instance of NumberModifier
number_modifier = NumberModifier(3)

# Get foreign key list from donors table
foreignkey_list = ContactAppender.getkeyDonor(cursor)

datalist= ContactAppender.generateContact(datalist,number_modifier,foreignkey_list)
ContactAppender.insertContacts(cursor,conn,datalist)