use Project
insert into BloodGroups values(1,'A+'),(2,'O+'),(3,'B+'),(4,'AB+'),(5,'A-'),(6,'O-'),(7,'B-'),(8,'AB-');
select * from BloodGroups
go
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(1, 1, 1), (2, 1, 5), (3, 1, 2), (4, 1, 6);

-- o+ can receive from o+ and o-
insert into Bloodgroup_Compatibilities (com_id, group_id, canreceive_id) values
(5, 2, 2), (6, 2, 6);

-- b+ can receive from b+, b-, o+, o-
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(7, 3, 3), (8, 3, 7), (9, 3, 2), (10, 3, 6);

-- ab+ can receive from everyone
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(11, 4, 1), (12, 4, 2), (13, 4, 3), (14, 4, 4), (15, 4, 5), (16, 4, 6), (17, 4, 7), (18, 4, 8);

-- a- can receive from a- and o-
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(19, 5, 5), (20, 5, 6);

-- o- can receive from o- only
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(21, 6, 6);

-- b- can receive from b- and o-
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(22, 7, 7), (23, 7, 6);

-- ab- can receive from ab-, a-, b-, o-
insert into bloodgroup_compatibilities (com_id, group_id, canreceive_id) values
(24, 8, 8), (25, 8, 5), (26, 8, 7), (27, 8, 6);
go
select
    bg1.GroupName as Blood_Groups,
    string_agg(bg2.GroupName, ', ') as Can_Receive_From
from
    BloodGroup_Compatibilities bgc
    join BloodGroups bg1 on bgc.group_id = bg1.Group_id
    join BloodGroups bg2 on bgc.canreceive_id = bg2.Group_id
group by
    bg1.GroupName
order by
    bg1.GroupName;


-- O group compatibility
INSERT INTO BloodGroup_Compatiblities_for_Plasma (cmp_id, BPgroup_id, canreceiveP_id) VALUES
(1, 1, 1),  -- O+ to O+
(2, 1, 2),  -- O+ to A+
(3, 1, 3),  -- O+ to B+
(4, 1, 4),  -- O+ to AB+
(5, 1, 5),  -- O+ to O-
(6, 1, 6),  -- O+ to A-
(7, 1, 7),  -- O+ to B-
(8, 1, 8);  -- O+ to AB-

-- A group compatibility
INSERT INTO BloodGroup_Compatiblities_for_Plasma (cmp_id, BPgroup_id, canreceiveP_id) VALUES
(9, 2, 2),  -- A+ to A+
(10, 2, 4), -- A+ to AB+
(11, 2, 6), -- A+ to A-
(12, 2, 8); -- A+ to AB-

-- B group compatibility
INSERT INTO BloodGroup_Compatiblities_for_Plasma (cmp_id, BPgroup_id, canreceiveP_id) VALUES
(13, 3, 3), -- B+ to B+
(14, 3, 4), -- B+ to AB+
(15, 3, 7), -- B+ to B-
(16, 3, 8); -- B+ to AB-

-- AB group compatibility
INSERT INTO BloodGroup_Compatiblities_for_Plasma (cmp_id, BPgroup_id, canreceiveP_id) VALUES
(17, 4, 4), -- AB+ to AB+
(18, 4, 8); -- AB+ to AB-
go
SELECT 
    p.GroupName AS PatientBloodGroup,
    d.GroupName AS DonorBloodGroup
FROM 
    BloodGroup_Compatiblities_for_Plasma c
JOIN 
    BloodGroups p ON c.BPgroup_id = p.Group_id
JOIN 
    BloodGroups d ON c.canreceiveP_id = d.Group_id
ORDER BY 
    p.GroupName, d.GroupName;


