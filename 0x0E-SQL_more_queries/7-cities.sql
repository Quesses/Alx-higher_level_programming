-- creates the database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch the active database
use hbtn_0d_usa;

-- creates the table 'cities' with several column contraints
-- unique id, auto generated, primary and cant be null
-- name cant be null and a state_id which is a foreign key
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE(id)
	FOREIGN KEY(state_id)
		REFERENCES states(id)
	);
