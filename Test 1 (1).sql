create database Project
go
use Project
go
create table Cell_Number(
CellNo_Id smallint, --pk
Number bigint,
Donor_CNIC bigint, --fk
constraint pk_cellNo primary key (CellNo_Id),
constraint fk_donor_id foreign key (Donor_CNIC) references Donors(CNIC)
);
go
create table Donors
(
CNIC bigint,  --pk
BloodGroup_Id int,
Date_Of_Birth date,
Province varchar(50),
City varchar(50),
Eligible varchar(3) check (Eligible in ('Yes','No')),
BloodType varchar(5) check(BloodType in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
constraint pk_donor_id primary key (CNIC)
);
go

create table Blood_Samples
(
Sample_id int, --pk
Donor_id bigint, --fk
Result varchar(1) check (Result in ('+','-'))
constraint pk_Sample primary key (Sample_id),
constraint fk_donorid_forSample foreign key (Donor_id) references Donors(CNIC)
);
go
create table BloodBanks(
License_id int,--pk
Telephone_Number bigint,
Name varchar(50),
Capacity int check (capacity > 0),
City varchar(50),
Street varchar (100),
Postal_Code int,
constraint pk_Bankid primary key(License_id)
);
go
create table BloodCellTypes(
BloodCell_id tinyint, --pk
BloodCell_Type varchar(10)
constraint pk_celltype primary key(BloodCell_id)
);
go
create table BloodUnits(
BloodUnit_id varchar(5), --pk
Blood_Group varchar(3) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
BloodCell_id tinyint, --fk
BloodBank_Id int, --fk
Donor_Id bigint,--fk
Storage_Date date default (getdate()),
Expiration_Date date,
constraint pk_bloodUnit_id primary key(BloodUnit_id),
constraint fk_BloodCellType_forUnit foreign key (BloodCell_id) references BloodCellTypes(BloodCell_id),
constraint fk_Bankid_forUnit foreign key (BloodBank_Id)  references BloodBanks(License_id),
constraint fk_Donorid_forUnit foreign key  (Donor_Id)  references Donors(CNIC)
);

go
create table Patients
(
CNIC bigint, --pk
Blood_Group varchar(3) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
Disease_or_Emergency varchar(100),
constraint pk_patienceCNIC primary key(CNIC)
);
go
create table Transfusions(
Transfusion_id int, --pk
patient_id bigint,--fk
Transfusion_Date date default (getdate()),
BloodUnit_id varchar(5)
constraint pk_tranfusionid primary key(Transfusion_id),
constraint fk_patient_id foreign key (patient_id) references Patients(CNIC),
constraint fk_bloodbank_id foreign key(BloodUnit_id) references BloodUnits(BloodUnit_id)
);
go

create table BloodGroups(
Group_id tinyint, --pk
GroupName varchar(3) check(GroupName in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
constraint pk_groupId primary key(Group_id)
);
go
create table BloodGroup_Compatibilities(
com_id tinyint,
group_id tinyint,
canreceive_id tinyint,
constraint pk_comid primary key(com_id),
constraint fk_group_id foreign key(group_id) references BloodGroups(Group_id),
constraint fk_receive_id foreign key(canreceive_id) references BloodGroups(Group_id)
);
create table BloodGroup_Compatiblities_for_Plasma(
cmp_id tinyint,
BPgroup_id tinyint,
canreceiveP_id tinyint,
constraint pk_cmpid primary key(cmp_id),
constraint fk_BPgroup_id foreign key(BPgroup_id) references BloodGroups(Group_id),
constraint fk_receiveP_id foreign key(canreceiveP_id) references BloodGroups(Group_id)
);


