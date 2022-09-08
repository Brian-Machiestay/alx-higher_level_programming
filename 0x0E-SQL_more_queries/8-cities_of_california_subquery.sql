--  lists all the cities of California
SELECT id, name
FROM
	(SELECT * FROM cities WHERE state_id =
		(SELECT id FROM states WHERE name = 'California')) AS name
