
--view to count number of avaiable blood types
SELECT bg.GroupName AS BloodType, COUNT(*) AS UnitsAvailable
FROM BloodUnits bu
INNER JOIN BloodGroups bg ON bu.Blood_Group = bg.GroupName
WHERE bu.unit_Status = 'Available'  -- Filter for available units only
GROUP BY bg.GroupName;
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
select * from [bloodunitdetails]
go
-- view to generate report on what blood banks have what blood units available
CREATE VIEW vw_BloodUnitReport
WITH SCHEMABINDING
AS
SELECT 
    Blood_Cell_Type,
    Blood_Group,
    Number_of_Units,
    Blood_Bank_Name
FROM (
    SELECT 
        BC.BloodCell_Type AS Blood_Cell_Type,
        BU.Blood_Group AS Blood_Group,
        COUNT(BU.BloodUnit_id) OVER (PARTITION BY BC.BloodCell_Type, BU.Blood_Group) AS Number_of_Units,
        BB.Name AS Blood_Bank_Name,
        ROW_NUMBER() OVER (PARTITION BY BC.BloodCell_Type, BU.Blood_Group ORDER BY BU.BloodUnit_id) AS Row_Num
    FROM 
        dbo.BloodUnits BU
    INNER JOIN 
        dbo.BloodCellTypes BC ON BU.BloodCell_id = BC.BloodCell_id
    LEFT JOIN 
        dbo.BloodBanks BB ON BU.bloodbank_id = BB.License_id
) AS subquery
WHERE Row_Num = 1;
--Test view
select * from vw_BloodUnitReport
---------------
go

---- view to display patients disease and its blood requirement corresponding to their disease
	WITH PatientSummary AS (
    SELECT
        P.name AS Patient_Name,
        P.CNIC AS Patient_CNIC,
        P.Disease_or_Emergency AS Patient_Disease,
        P.Blood_Group AS Required_Blood_Type,
        BC.BloodCell_Type AS Required_Blood_Cell_Type,
        BG.GroupName AS Compatible_Blood_Type,
        BGP.GroupName AS Compatible_Plasma_Type,
        ROW_NUMBER() OVER (PARTITION BY P.name ORDER BY P.CNIC) AS RowNum
    FROM
        Patients P
    JOIN
        BloodGroups BG ON P.Blood_Group = BG.GroupName
    JOIN
        BloodUnits BU ON P.Blood_Group = BU.Blood_Group
    JOIN
        BloodCellTypes BC ON BU.BloodCell_id = BC.BloodCell_id
    JOIN
        BloodGroup_Compatibilities BGC ON BG.Group_id = BGC.group_id
    JOIN
        BloodGroups CompatibleBG ON BGC.canreceive_id = CompatibleBG.Group_id
    JOIN
        BloodGroup_Compatiblities_for_Plasma BGCP ON BG.Group_id = BGCP.BPgroup_id
    JOIN
        BloodGroups BGP ON BGCP.canreceiveP_id = BGP.Group_id
)
SELECT 
    Patient_Name,
    Patient_CNIC,
    Patient_Disease,
    Required_Blood_Type,
    Required_Blood_Cell_Type,
    Compatible_Blood_Type,
    Compatible_Plasma_Type
FROM 
    PatientSummary
WHERE 
    RowNum = 1
ORDER BY 
    Patient_Name;
go
------------Testing

-- CTE to get filtered patient details with the specified diseases
WITH FilteredPatients AS (
    SELECT
        P.name AS Patient_Name,
        P.CNIC AS Patient_CNIC,
        P.Disease_or_Emergency AS Patient_Disease,
        P.Blood_Group AS Required_Blood_Type
    FROM
        Patients P
    WHERE
        P.Disease_or_Emergency IN ('Thalassemia', 'Leukemia', 'Lymphoma', 'Multiple Myeloma', 'Hemophilia')
),
-- CTE to calculate disease statistics and percentage
DiseaseStatistics AS (
    SELECT
        Patient_Disease,
        COUNT(*) AS DiseaseCount,
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS DiseasePercentage
    FROM
        FilteredPatients
    GROUP BY
        Patient_Disease
),
-- CTE to get unique blood units with blood banks information and blood cell types
UniqueBloodUnits AS (
    SELECT DISTINCT
        BU.Blood_Group,
        BU.BloodUnit_id,
        BU.BloodCell_id,
        BC.BloodCell_Type,
        BB.License_id AS Bank_id,
        BB.Name AS BankName,
        BB.City
    FROM
        BloodUnits BU
    JOIN
        BloodBanks BB ON BU.bloodbank_id = BB.License_id
    JOIN
        BloodCellTypes BC ON BU.BloodCell_id = BC.BloodCell_id
)

-- Final SELECT to combine disease statistics and blood unit availability
SELECT DISTINCT
    DS.Patient_Disease,
    DS.DiseaseCount,
    DS.DiseasePercentage,
    BU.Blood_Group AS Required_Blood_Type,
    BU.BloodCell_Type AS Required_Blood_Cell_Type,
    BU.BloodUnit_id,
    BU.Bank_id,
    BU.BankName,
    BU.City
FROM
    DiseaseStatistics DS
JOIN
    FilteredPatients FP ON DS.Patient_Disease = FP.Patient_Disease
JOIN
    UniqueBloodUnits BU ON FP.Required_Blood_Type = BU.Blood_Group
ORDER BY
    DS.Patient_Disease, BU.BloodUnit_id;
	go
	------------------------------



	CREATE VIEW DiseaseBloodAvailability AS
WITH FilteredPatients AS (
    SELECT
        P.name AS Patient_Name,
        P.CNIC AS Patient_CNIC,
        P.Disease_or_Emergency AS Patient_Disease,
        P.Blood_Group AS Required_Blood_Type
    FROM
        Patients P
    WHERE
        P.Disease_or_Emergency IN ('Thalassemia', 'Leukemia', 'Lymphoma', 'Multiple Myeloma', 'Hemophilia')
),
DiseaseStatistics AS (
    SELECT
        Patient_Disease,
        COUNT(*) AS DiseaseCount,
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS DiseasePercentage
    FROM
        FilteredPatients
    GROUP BY
        Patient_Disease
),
UniqueBloodUnits AS (
    SELECT DISTINCT
        BU.Blood_Group,
        BU.BloodUnit_id,
        BU.BloodCell_id,
        BC.BloodCell_Type,
        BB.License_id AS Bank_id,
        BB.Name AS BankName,
        BB.City
    FROM
        BloodUnits BU
    JOIN
        BloodBanks BB ON BU.bloodbank_id = BB.License_id
    JOIN
        BloodCellTypes BC ON BU.BloodCell_id = BC.BloodCell_id
)
SELECT DISTINCT
    DS.Patient_Disease,
    DS.DiseaseCount,
    DS.DiseasePercentage,
    BU.Blood_Group AS Required_Blood_Type,
    BU.BloodCell_Type AS Required_Blood_Cell_Type,
    BU.BloodUnit_id,
    BU.Bank_id,
    BU.BankName,
    BU.City
FROM
    DiseaseStatistics DS
JOIN
    FilteredPatients FP ON DS.Patient_Disease = FP.Patient_Disease
JOIN
    UniqueBloodUnits BU ON FP.Required_Blood_Type = BU.Blood_Group;
	---------Testing View----------------------------

	select * from DiseaseBloodAvailability
	where City= 'Lahore'