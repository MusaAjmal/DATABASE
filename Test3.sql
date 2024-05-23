
CREATE PROCEDURE InsertDonor (
  @DonorCNIC varchar(50),
  @BloodGroupId int,
  @DateOfBirth date,
  @Province varchar(50),
  @City varchar(50),
  @BloodType varchar(5)
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO Donor (CNIC, BloodGroup_Id, Date_Of_Birth, Province, City, BloodType)
    VALUES (@DonorCNIC, @BloodGroupId, @DateOfBirth, @Province, @City, @BloodType);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage nvarchar(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertCellNumber (
  @CellNoId int,
  @Number varchar(100),
  @DonorCNIC varchar(50)
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO Cell_Numbers (CellNo_Id, Number, Donor_CNIC)
    VALUES (@CellNoId, @Number, @DonorCNIC);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage nvarchar(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodSample (
  @Sample_Id INT,
  @Donor_Id VARCHAR(50),
  @Eligibility VARCHAR(10)
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO Blood_Samples (Sample_Id, Donor_Id, Eligibility)
    VALUES (@Sample_Id, @Donor_Id, @Eligibility);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodBank (
  @License_Id INT,
  @Telephone_Number VARCHAR(50),
  @Name VARCHAR(50),
  @Capacity INT,
  @City VARCHAR(50),
  @Street VARCHAR(100),
  @Postal_Code INT
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO BloodBanks(License_Id, Telephone_Number, Name, Capacity, City, Street, Postal_Code)
    VALUES (@License_Id, @Telephone_Number, @Name, @Capacity, @City, @Street, @Postal_Code);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodCellType (
  @BloodCell_Id INT,
  @BloodCell_Type VARCHAR(50)
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO BloodCellTypes (BloodCell_Id, BloodCell_Type)
    VALUES (@BloodCell_Id, @BloodCell_Type);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodUnit (
  @BloodUnit_Id INT,
  @Blood_Group VARCHAR(5),
  @BloodCell_Id INT,
  @BloodBank_Id INT,
  @Donor_Id VARCHAR(50),
  @Storage_Date DATE,
  @Expiry_Date DATE
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO BloodUnits(BloodUnit_Id, Blood_Group, BloodCell_Id, BloodBank_Id, Donor_Id, Storage_Date, Expiry_Date)
    VALUES (@BloodUnit_Id, @Blood_Group, @BloodCell_Id, @BloodBank_Id, @Donor_Id, @Storage_Date, @Expiry_Date);
	
    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertTransfusion (
  @Transfusion_Id INT,
  @Patient_Id VARCHAR(50),
  @Transfusion_Date DATE
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO Transfusions (Transfusion_Id, Patient_Id, Transfusion_Date)
    VALUES (@Transfusion_Id, @Patient_Id, @Transfusion_Date);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertPatient (
  @CNIC VARCHAR(50),
  @Blood_Group VARCHAR(5),
  @Disease_or_Emergency VARCHAR(1000)
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO Patients (CNIC, Blood_Group, Disease_or_Emergency)
    VALUES (@CNIC, @Blood_Group, @Disease_or_Emergency);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodGroup (
  @Group_Id INT,
  @GroupName VARCHAR(5)
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO BloodGroups (Group_Id, GroupName)
    VALUES (@Group_Id, @GroupName);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodGroupCompatibility (
  @Com_Id INT,
  @Group_Id INT,
  @CanReceive_Id INT
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO BloodGroup_Compatibilities (Com_Id, Group_Id, CanReceive_Id)
    VALUES (@Com_Id, @Group_Id, @CanReceive_Id);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
CREATE PROCEDURE InsertBloodGroupCompatibilities_for_Plasma (
  @Cmp_Id INT,
  @BPgroup_Id INT,
  @CanReceiveP_Id INT
)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;

    INSERT INTO BloodGroup_Compatiblities_for_Plasma (Cmp_Id, BPgroup_Id, CanReceiveP_Id)
    VALUES (@Cmp_Id, @BPgroup_Id, @CanReceiveP_Id);

    COMMIT;
  END TRY
  BEGIN CATCH
    IF @@ERROR <> 0
    BEGIN
      DECLARE @ErrorMessage NVARCHAR(4000);
      SELECT @ErrorMessage = ERROR_MESSAGE();
      RAISERROR (@ErrorMessage, 16, 1);
      ROLLBACK TRANSACTION;
    END
  END CATCH
END;
go
---Trigger for reducing capacity whenever data is inserted inside the inventory
CREATE TRIGGER UpdateBloodBankCapacity
ON BloodUnits -- Trigger on the Inventory table
  AFTER INSERT -- Fires after INSERT operation
AS
BEGIN
  DECLARE @BloodBankId INT;
  DECLARE @NewCapacity INT;

  -- Get the BloodBankId from the inserted row
  SELECT @BloodBankId = BloodBank_Id FROM INSERTED;

  -- Get the current capacity of the BloodBank
  SELECT @NewCapacity = Capacity - 1
  FROM BloodBanks
  WHERE License_Id = @BloodBankId; -- Use foreign key reference

  -- Update the BloodBank capacity (if a record is found)
  IF @@ROWCOUNT > 0
  BEGIN
    UPDATE BloodBanks
    SET Capacity = @NewCapacity
    WHERE License_Id = @BloodBankId;
  END
END;
go
SELECT 
  o.name AS Procedure_Name,
  OBJECT_DEFINITION(o.[object_id]) AS Procedure_Definition
FROM sys.objects o
WHERE o.type IN ('P', 'PC') -- Filter for procedures and stored procedures
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
