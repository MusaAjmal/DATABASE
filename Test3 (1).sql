use Project


SELECT 
  o.name AS Procedure_Name,
  OBJECT_DEFINITION(o.[object_id]) AS Procedure_Definition
FROM sys.objects o
WHERE o.type ='PC' -- Filter for procedures and stored procedures
ORDER BY Procedure_Name;
go
SELECT 
    trig.name AS TriggerName,
    OBJECT_NAME(trig.parent_id) AS TableName,
    trig.create_date AS CreationDate,
    trig.modify_date AS LastModifiedDate,
    OBJECT_DEFINITION(trig.object_id) AS TriggerDefinition
FROM 
    sys.triggers AS trig
INNER JOIN 
    sys.objects AS obj ON trig.parent_id = obj.object_id
WHERE 
    trig.is_ms_shipped = 0;

go
delete from Donors
delete from Cell_Number
go
delete from blood_samples
select * from donors
select * from BloodBanks
select * from Cell_Number
select * from Blood_Samples
go
CREATE VIEW BloodUnitDetails AS
SELECT 
    BloodUnits.BloodUnit_id AS UnitID,
    Donors.CNIC AS DonorCNIC,
    BloodUnits.bloodbank_id AS BankID,
    BloodCellTypes.BloodCell_Type AS CellType,
    BloodUnits.Storage_Date AS StartDate,
    BloodUnits.Expiration_Date AS EndDate,
    BloodUnits.unit_status AS Status
FROM 
    BloodUnits
JOIN 
    Donors ON BloodUnits.Donor_Id = Donors.CNIC
JOIN 
    BloodCellTypes ON BloodUnits.BloodCell_id = BloodCellTypes.BloodCell_id
LEFT JOIN 
    BloodBanks ON BloodUnits.bloodbank_id = BloodBanks.License_id;

go
select * from Transfusions
select * from patients
select * from Cell_Number
insert into BloodCellTypes values(1,'Red Blood'),(2,'Plasma'),(3,'Platelets')

select * from BloodUnits
SELECT
    D.CNIC,
    D.Donor_Name,
    D.Date_Of_Birth,
    D.Province,
    D.City,
    D.Eligible,
    D.BloodType,
    CN.Number AS Cell_Number
FROM
    Donors D
JOIN
    Cell_Number CN ON D.CNIC = CN.Donor_CNIC
WHERE
    D.Eligible = 'Yes' and City ='Lahore'
ORDER BY
    D.CNIC;
go
SELECT 
    d.Donor_Name,
    bs.Result
FROM 
    Donors d
JOIN 
    Blood_Samples bs
ON 
    d.CNIC = bs.Donor_id
WHERE 
    bs.Result = '+';
go