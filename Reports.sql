--count number of avaiable blood types
SELECT bg.GroupName AS BloodType, COUNT(*) AS UnitsAvailable
FROM BloodUnits bu
INNER JOIN BloodGroups bg ON bu.Blood_Group = bg.GroupName
WHERE bu.unit_Status = 'Available'  -- Filter for available units only
GROUP BY bg.GroupName;
go

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
select * from vw_BloodUnitReport
---------------
go
CREATE PROCEDURE PerformBloodTransfusion
    @patientCNIC VARCHAR(13)
AS
BEGIN
    DECLARE @patientBloodGroup VARCHAR(3)
    DECLARE @transfusionID INT
    
    -- Get patient's blood group
    SELECT @patientBloodGroup = Blood_Group
    FROM Patients
    WHERE CNIC = @patientCNIC
    
    IF @patientBloodGroup IS NOT NULL
    BEGIN
        -- Determine compatible blood groups
        DECLARE @compatibleBloodGroups TABLE (GroupName VARCHAR(3))
        
        INSERT INTO @compatibleBloodGroups (GroupName)
        SELECT BG2.GroupName
        FROM BloodGroups BG1
        INNER JOIN BloodGroup_Compatibilities BC ON BG1.Group_id = BC.group_id
        INNER JOIN BloodGroups BG2 ON BC.canreceive_id = BG2.Group_id
        WHERE BG1.GroupName = @patientBloodGroup
        
        -- Get the transfusion ID
        SET @transfusionID = (SELECT ISNULL(MAX(Transfusion_id), 0) + 1 FROM Transfusions)
        
        -- Select available compatible blood units
        INSERT INTO Transfusions (Transfusion_id, patient_id, Transfusion_Date, bloodunit_id)
        SELECT @transfusionID, @patientCNIC, GETDATE(), BU.BloodUnit_id
        FROM BloodUnits BU
        INNER JOIN @compatibleBloodGroups CBG ON BU.Blood_Group = CBG.GroupName
        WHERE BU.unit_status = 'Available'
        ORDER BY BU.Expiration_Date ASC
        
        -- Mark the selected blood unit as used
        UPDATE BloodUnits
        SET unit_status = 'Expired'
        WHERE BloodUnit_id = (SELECT TOP 1 BloodUnit_id FROM Transfusions WHERE patient_id = @patientCNIC)
    END
    ELSE
    BEGIN
        PRINT 'Patient not found or blood group information missing.'
    END
END

----
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



