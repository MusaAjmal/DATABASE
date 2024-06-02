CREATE PROCEDURE DonateBloodToBank
    @Donor_CNIC varchar(13),
    @Blood_Bank_License_id int,
    @Blood_Group varchar(3),
    @Blood_Cell_Type tinyint,
    @Expiration_Date date,
	@unitid varchar(5)
AS
BEGIN
    SET NOCOUNT ON;

    -- Check if the donor is eligible
    DECLARE @IsEligible varchar(3);
    SELECT @IsEligible = Eligible
    FROM Donors
    WHERE CNIC = @Donor_CNIC;

    IF @IsEligible = 'Yes'
    BEGIN
        -- Insert into BloodUnits table
        INSERT INTO BloodUnits (BloodUnit_id, Blood_Group, BloodCell_id, bloodbank_id, Storage_Date, Expiration_Date, unit_status)
        VALUES (@unitid, @Blood_Group, @Blood_Cell_Type, @Blood_Bank_License_id, GETDATE(), @Expiration_Date, 'Available');

        PRINT 'Blood donated successfully and stored in the blood bank inventory.';
    END
    ELSE
    BEGIN
        PRINT 'Donor is not eligible to donate blood.';
    END
END
exec donatebloodtobank '1165768819974', 1, 'A+', 1, '2024-06-30','dqd21';

go
select * from Donors
CREATE PROCEDURE performbloodtransfusion
    @patientcnic VARCHAR(13),
    @transfusionid INT
AS
BEGIN
    DECLARE @patientbloodgroup VARCHAR(3);
    
    -- Fetch the patient's blood group
    SELECT @patientbloodgroup = blood_group
    FROM patients
    WHERE cnic = @patientcnic;
    
    -- Check if the patient's blood group was found
    IF @patientbloodgroup IS NOT NULL
    BEGIN
        -- Create a table to store compatible blood groups
        DECLARE @compatiblebloodgroups TABLE (groupname VARCHAR(3));
        
        -- Insert compatible blood groups into the table
        INSERT INTO @compatiblebloodgroups (groupname)
        SELECT bg2.groupname
        FROM bloodgroups bg1
        INNER JOIN bloodgroup_compatibilities bc ON bg1.group_id = bc.group_id
        INNER JOIN bloodgroups bg2 ON bc.canreceive_id = bg2.group_id
        WHERE bg1.groupname = @patientbloodgroup;
        
        -- Insert a new transfusion record for the patient using the first available compatible blood unit
        INSERT INTO transfusions (Transfusion_id, patient_id, transfusion_date, bloodunit_id)
        SELECT TOP 1 @transfusionid, @patientcnic, GETDATE(), bu.bloodunit_id
        FROM bloodunits bu
        INNER JOIN @compatiblebloodgroups cbg ON bu.blood_group = cbg.groupname
        WHERE bu.unit_status = 'Available'
        ORDER BY bu.expiration_date ASC;
        
        -- Update the status of the blood unit used in the transfusion to 'Expired'
        UPDATE bloodunits
        SET unit_status = 'Expired'
        WHERE bloodunit_id = (SELECT TOP 1 bloodunit_id FROM transfusions WHERE Transfusion_id = @transfusionid);
    END
    ELSE
    BEGIN
        PRINT 'Patient not found or blood group information missing.';
    END
END;

select * from Patients
exec performbloodtransfusion '1177946719158',3129318


----
CREATE PROCEDURE GetBloodUnitsByBankAndGroup
    @Blood_Group VARCHAR(3),
	@city varchar(50)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT bb.License_id, bb.Name, bu.*
    FROM BloodBanks bb
    INNER JOIN BloodUnits bu ON bb.License_id = bu.bloodbank_id
    WHERE bu.Blood_Group = @Blood_Group and bb.City=@city
END;
select * from BloodBanks
exec GetBloodUnitsByBankAndGroup 'B+','Lahore'
GO
CREATE PROCEDURE GetDonorDetailsByBloodGroupAndCity
    @Blood_Group VARCHAR(5),
    @City VARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        Donors.Donor_Name,
        Donors.CNIC,
        Donors.Date_Of_Birth,
        Donors.Province,
        Donors.City,
        Donors.Eligible,
        Donors.BloodType,
        Cell_Number.Number AS ContactNo
    FROM Donors
    LEFT JOIN Cell_Number ON Donors.CNIC = Cell_Number.Donor_CNIC
    WHERE Donors.BloodType = @Blood_Group
      AND Donors.City = @City;
END;

exec GetDonorDetailsByBloodGroupAndCity 'A+','Lahore'