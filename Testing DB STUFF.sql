use Project

--checking our procedures
SELECT 
  o.name AS Procedure_Name,
  OBJECT_DEFINITION(o.[object_id]) AS Procedure_Definition
FROM sys.objects o
WHERE o.type ='PC' -- Filter for procedures and stored procedures
ORDER BY Procedure_Name;
go
-- checking our triggers
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


