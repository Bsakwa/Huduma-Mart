-- CREATES a new MYSQL server database hbnb_test_db
-- CREATES a new user hbnb_test
-- SETS user password to hbnb_test_pwd
-- USER should have all the priviledges only on this database
-- USER should have SELECT priviledge on databasee performance_schema

CREATE DATABASE IF NOT EXISTS huduma_db;
CREATE  USER 
	IF NOT EXISTS 'huduma_dev'@'localhost' 
	IDENTIFIED BY 'huduma_dev_pwd';
GRANT ALL PRIVILEGES
	ON `huduma_db`.* TO 'huduma_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'huduma_dev'@'localhost';
FLUSH PRIVILEGES;
