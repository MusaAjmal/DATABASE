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

