-- CREATES a new MYSQL server database huduma_db
-- CREATES a new user huduma_dev
-- SETS user password to huduma_dev_pwd
-- USER should have all the priviledges only on this database
-- USER should have SELECT priviledge on database performance_schema

CREATE DATABASE IF NOT EXISTS huduma_db;
CREATE  USER 
	IF NOT EXISTS 'huduma_dev'@'localhost' 
	IDENTIFIED BY 'huduma_dev_pwd';
GRANT ALL PRIVILEGES
	ON `huduma_db`.* TO 'huduma_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'huduma_dev'@'localhost';
FLUSH PRIVILEGES;
