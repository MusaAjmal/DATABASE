-- A trigger to make sure that a person can donate blood once per 3 months
CREATE TRIGGER update_eligibility
ON Blood_Samples
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE Donors
    SET Eligible = 'No'
    FROM Donors
    INNER JOIN inserted ON Donors.CNIC = inserted.Donor_id
    WHERE inserted.Result = '+';
END;
go
--backup/history table in case data gets deleted
CREATE TRIGGER trg_DeleteBloodBank_MoveToBackup
ON BloodBanks
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;

    -- Insert deleted rows into Backup_BloodBanks table
    INSERT INTO Backup_BloodBanks (backup_License_id, Telephone_Number, Name, Capacity, City, Street, Postal_Code)
    SELECT License_id, Telephone_Number, Name, Capacity, City, Street, Postal_Code
    FROM deleted;
END;
--Making sure that expired blood unit is no obtainable 
go
CREATE TRIGGER set_unit_unavailable
ON BloodUnits
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE BloodUnits
    SET unit_status = 'Expired'
    WHERE Expiration_Date <= GETDATE() AND unit_status = 'Available';
END;


--testing
update bloodunits
set Expiration_Date=getdate()
where BloodUnit_id='07CJI'

go
-- backup table for blood unit
CREATE TRIGGER trg_UpdateBackupBloodUnit
ON BloodUnits
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;

    -- Insert deleted BloodUnits data into Backup_BloodUnits
    INSERT INTO Backup_BloodUnits (
        backup_BloodUnit_id,
        Blood_Group,
        BloodCell_id,
        bloodbank_id,
        backup_bloodbank_id,
        Donor_Id,
        Storage_Date,
        Expiration_Date
    )
    SELECT 
        BloodUnit_id,
        Blood_Group,
        BloodCell_id,
        bloodbank_id,
        backup_BloodBank_Id,
        Donor_Id,
        Storage_Date,
        Expiration_Date
    FROM 
        deleted;

    
END;
go
--  Update the status of certain units to 'Expired' after each transfusion 
CREATE TRIGGER trg_AfterInsertTransfusions_UpdateStatus
ON Transfusions
AFTER INSERT
AS
BEGIN
    
    UPDATE BloodUnits
    SET unit_status = 'Expired'
    WHERE BloodUnit_id IN (
        SELECT inserted.bloodunit_id
        FROM inserted
    );
END;
go
--only non-expired/ non-used blood units must be obtainable
CREATE TRIGGER trg_BeforeInsertTransfusions_CheckParentStatus
ON Transfusions
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1
        FROM inserted i
        WHERE NOT EXISTS (
            SELECT 1
            FROM BloodUnits bu
            WHERE bu.BloodUnit_id = i.bloodunit_id
            AND bu.unit_status = 'Available'
        )
    )
    BEGIN
        RAISERROR ('Cannot insert. One or more units are not available.', 16, 1)
        ROLLBACK TRANSACTION
    END
    ELSE
    BEGIN
        
        INSERT INTO Transfusions (Transfusion_id, patient_id, Transfusion_Date, bloodunit_id, backup_BloodUnit_id)
        SELECT Transfusion_id, patient_id, Transfusion_Date, bloodunit_id, backup_BloodUnit_id
        FROM inserted;
    END
END;

--Test--
select * from Transfusions
insert into Transfusions values(12313164,'1233336869498','2024-05-31','T6DPG',null)
--------------------------------------


