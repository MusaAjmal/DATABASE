create database Project
go
use Project
go
create table Cell_Number(
CellNo_Id int, --pk
Number varchar(11),
Donor_CNIC varchar(13) --fk
constraint pk_cellNo primary key (CellNo_Id)
constraint fk_donor_id foreign key (Donor_CNIC) references Donors(CNIC)
);
go
create table Donors
(
CNIC varchar(13),  --pk
BloodGroup_Id int,
Date_Of_Birth date,
Province varchar(50),
City varchar(50),
Eligibility varchar(10) check (Eligibility in ('Yes','No')),
BloodType varchar(5) check(BloodType in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
constraint pk_donor_id primary key (CNIC)
);
go
create table Blood_Samples
(
Sample_id int, --pk
Donor_id varchar(13), --fk
Eligibility varchar(10) check (Eligibility in ('Yes','No'))
constraint pk_Sample primary key (Sample_id),
constraint fk_donorid_forSample foreign key (Donor_id) references Donors(CNIC)
);
go
create table BloodBanks(
License_id int,--pk
Telephone_Number varchar(50),
Name varchar(50),
Capacity int check (capacity > 0),
City varchar(50),
Street varchar (100),
Postal_Code int,
constraint pk_Bankid primary key(License_id)
);
go
create table BloodCellTypes(
BloodCell_id int, --pk
BloodCell_Type varchar(50)
constraint pk_celltype primary key(BloodCell_id)
);
go
create table BloodUnits(
BloodUnit_id int, --pk
Blood_Group varchar(5) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
BloodCell_id int, --fk
BloodBank_Id int, --fk
Donor_Id varchar (13),--fk
Storage_Date date default (getdate()),
Expiration_Date date,
constraint pk_bloodUnit_id primary key(BloodUnit_id),
constraint fk_BloodCellType_forUnit foreign key (BloodCell_id) references BloodCellTypes(BloodCell_id),
constraint fk_Bankid_forUnit foreign key (BloodBank_Id)  references BloodBanks(License_id),
constraint fk_Donorid_forUnit foreign key  (Donor_Id)  references Donors(CNIC)
);

go
create table Transfusions(
Transfusion_id int, --pk
patient_id varchar(13),--fk
Transfusion_Date date,
bank_id int
constraint pk_tranfusionid primary key(Transfusion_id),
constraint fk_patient_id foreign key (patient_id) references Patients(CNIC),
constraint fk_bloodbank_id foreign key(bank_id) references BloodUnits(BloodUnit_id)
);
go
create table Patients
(
CNIC varchar(13), --pk
Blood_Group varchar(5) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
Disease_or_Emergency varchar(1000),
constraint pk_patienceCNIC primary key(CNIC)
);
go
create table BloodGroups(
Group_id int, --pk
GroupName varchar(5) check(GroupName in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
constraint pk_groupId primary key(Group_id)
);
go
create table BloodGroup_Compatibilities(
com_id int,
group_id int,
canreceive_id int,
constraint pk_comid primary key(com_id),
constraint fk_group_id foreign key(group_id) references BloodGroups(Group_id),
constraint fk_receive_id foreign key(canreceive_id) references BloodGroups(Group_id)
);
create table BloodGroup_Compatiblities_for_Plasma(
cmp_id int,
BPgroup_id int,
canreceiveP_id int,
constraint pk_cmpid primary key(cmp_id),
constraint fk_BPgroup_id foreign key(BPgroup_id) references BloodGroups(Group_id),
constraint fk_receiveP_id foreign key(canreceiveP_id) references BloodGroups(Group_id)
);


