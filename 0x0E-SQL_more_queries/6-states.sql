-- creates the database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch the active database
use hbtn_0d_usa;

-- creates the table 'states' with several column contraints
-- unique id, auto generated, primary and cant be null
-- name cant be null
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
	UNIQUE(id)
	);
