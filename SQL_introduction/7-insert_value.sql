-- Script inserts rows in database
INSERT INTO first_table (id, name)
VALUES (89, 'Best School')-- Script displays number of records with id == 89
SELECT count(*)
AS record_count
FROM first_table
WHERE id = 89;