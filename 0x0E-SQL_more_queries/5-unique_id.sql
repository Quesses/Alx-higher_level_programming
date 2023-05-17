-- creates the table 'unique_id' with a column contraints
-- unique id default 1 and name must not be null
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE(id)
	);
