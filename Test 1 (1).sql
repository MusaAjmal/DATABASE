create database Project
go
use Project
go
create table Donors
(
CNIC varchar(13) CHECK (LEN(CNIC) = 13 AND CNIC LIKE '[1-9][0-9-]%' AND CNIC NOT LIKE '%[^0-9-]%'),--pk
Donor_Name varchar(50),
BloodGroup_Id int,
Date_Of_Birth date,
Province varchar(50),
City varchar(50),
Eligible varchar(3) check (Eligible in ('Yes','No')),
BloodType varchar(5) check(BloodType in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
constraint pk_donor_id primary key (CNIC)
);
go
create table Cell_Number(
CellNo_Id smallint, --pk
Number bigint,
Donor_CNIC varchar(13) check (LEN(Donor_CNIC) = 13 AND Donor_CNIC LIKE '[1-9][0-9-]%' AND Donor_CNIC NOT LIKE '%[^0-9-]%'), --fk
constraint pk_cellNo primary key (CellNo_Id),
constraint fk_donor_id foreign key (Donor_CNIC) references Donors(CNIC) on delete cascade
);

go

create table Blood_Samples
(
Sample_id int, --pk
Donor_id varchar(13) check (LEN(Donor_id) = 13 AND Donor_id LIKE '[1-9][0-9-]%' AND Donor_id NOT LIKE '%[^0-9-]%'), --fk
Result varchar(1) check (Result in ('+','-'))
constraint pk_Sample primary key (Sample_id),
constraint fk_donorid_forSample foreign key (Donor_id) references Donors(CNIC) on delete cascade
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
create table Backup_BloodBanks(
backup_License_id int,--pk
Telephone_Number bigint,
Name varchar(50),
City varchar(50),
Street varchar (100),
Postal_Code int,
constraint pk_Bankid_backup primary key(backup_License_id)
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
backup_BloodBank_Id int,
Donor_Id varchar(13) check (LEN(Donor_id) = 13 AND Donor_id LIKE '[1-9][0-9-]%' AND Donor_id NOT LIKE '%[^0-9-]%'),--fk
Storage_Date date default (getdate()),
Expiration_Date date,
constraint pk_bloodUnit_id primary key(BloodUnit_id),
constraint fk_BloodCellType_forUnit foreign key (BloodCell_id) references BloodCellTypes(BloodCell_id),
constraint fk_Bankid_forUnit_backup foreign key (backup_BloodBank_Id)  references Backup_BloodBanks(backup_License_id) on delete cascade,
constraint fk_Donorid_forUnit foreign key  (Donor_Id)  references Donors(CNIC) on delete set null
);
go
create table Backup_BloodUnits(
backup_BloodUnit_id varchar(5), --pk
Blood_Group varchar(3) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
BloodCell_id tinyint, --fk
BloodBank_Id int, --fk
backup_bloodbank_id int,
Donor_Id varchar(13) check (LEN(Donor_id) = 13 AND Donor_id LIKE '[1-9][0-9-]%' AND Donor_id NOT LIKE '%[^0-9-]%'),--fk
Storage_Date date default (getdate()),
Expiration_Date date,
constraint pk_bloodUnit_id_backup primary key(backup_BloodUnit_id),
constraint fk_bloodcelltype_forunit_backup foreign key (bloodcell_id) references bloodcelltypes(bloodcell_id),
constraint fk_backup_bloodbankid_forunit_nobackup foreign key (bloodbank_id) references bloodbanks(license_id) on delete set null,
constraint fk_bloodbankid_forunit_backup foreign key (backup_bloodbank_id) references backup_bloodbanks(backup_license_id) on delete cascade,
constraint fk_donorid_forunit_backup foreign key (donor_id) references donors(cnic) on delete set null
);
go
create table Patients
(
CNIC varchar (13) check (LEN(CNIC) = 13 AND CNIC LIKE '[1-9][0-9-]%' AND CNIC NOT LIKE '%[^0-9-]%'), --pk
Blood_Group varchar(3) check(Blood_Group in('A+','O+','B+','AB+','A-','O-','B-','AB-')),
Disease_or_Emergency varchar(100),
constraint pk_patienceCNIC primary key(CNIC)
);
go
create table Transfusions(
Transfusion_id int, --pk
patient_id varchar(13) check (LEN(patient_id) = 13 AND patient_id LIKE '[1-9][0-9-]%' AND patient_id NOT LIKE '%[^0-9-]%'),--fk
Transfusion_Date date default (getdate()),
BloodUnit_id varchar(5),
backup_BloodUnit_id varchar(5)
constraint pk_tranfusionid primary key(Transfusion_id),
constraint fk_patient_id foreign key (patient_id) references Patients(CNIC),
constraint fk_bloodbank_id foreign key(BloodUnit_id) references BloodUnits(BloodUnit_id) on delete set null,
constraint fk_bloodbank_id_backup foreign key(backup_BloodUnit_id) references Backup_BloodUnits(backup_BloodUnit_id)
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

