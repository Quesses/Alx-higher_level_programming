-- creates the table 'id_not_null' with a column contraints
-- id default 1 and name must not be null
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL
	);
