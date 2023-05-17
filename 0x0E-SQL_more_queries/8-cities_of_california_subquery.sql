-- lists all the cities of California in a table
-- result sorted in ascending order by cities.id
SELECT id, name FROM cities
	WHERE state_id IN
	(
		SELECT id FROM states
			WHERE name = 'California'
	)
	ORDER BY id ASC;
