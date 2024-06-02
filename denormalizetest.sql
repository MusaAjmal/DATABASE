CREATE TABLE Combined_Table
(
    CNIC varchar(13),
    Donor_Name varchar(50),
    Date_Of_Birth date,
    Province varchar(50),
    City varchar(50),
    Eligible varchar(3),
    BloodType varchar(5),
    CellNo_Id smallint,
    Number bigint,
    Donor_CNIC varchar(13),
    Sample_id int,
    Donor_id varchar(13),
    Result varchar(1),
    License_id int,
    Telephone_Number bigint,
    Name varchar(50),
    Capacity int,
    Street varchar(100),
    Postal_Code int,
    backup_License_id int,
    BloodCell_id tinyint,
    bloodbank_id int,
    backup_BloodBank_Id int,
    Storage_Date date,
    Expiration_Date date,
    unit_status varchar(15),
    backup_BloodUnit_id varchar(5),
    patient_id varchar(13),
    Transfusion_id int,
    Transfusion_Date date,
    bloodunit_id varchar(5),
    backup_BloodUnit_id2 varchar(5),
    Group_id tinyint,
    GroupName varchar(3),
    com_id tinyint,
    canreceive_id tinyint,
    cmp_id tinyint,
    BPgroup_id tinyint,
    canreceiveP_id tinyint
);
select * from Combined_Table
go
SELECT *
FROM Donors d
LEFT JOIN Cell_Number cn ON d.CNIC = cn.Donor_CNIC
LEFT JOIN Blood_Samples bs ON d.CNIC = bs.Donor_id
LEFT JOIN BloodUnits bu ON d.CNIC = bu.Donor_Id
LEFT JOIN BloodBanks bb ON bu.bloodbank_id = bb.License_id
LEFT JOIN Backup_BloodBanks bbb ON bu.backup_BloodBank_Id = bbb.backup_License_id
LEFT JOIN Backup_BloodUnits bbu ON d.CNIC = bbu.Donor_Id
LEFT JOIN Patients p ON d.CNIC = p.CNIC
LEFT JOIN Transfusions t ON p.CNIC = t.patient_id
LEFT JOIN BloodGroups bg ON bu.Blood_Group = bg.GroupName
LEFT JOIN BloodCellTypes bct ON bu.BloodCell_id = bct.BloodCell_id
LEFT JOIN BloodGroup_Compatibilities bgc ON bgc.group_id = bg.Group_id
LEFT JOIN BloodGroup_Compatiblities_for_Plasma bgcp ON bgcp.BPgroup_id = bg.Group_id
