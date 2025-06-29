-- this script creates a new database and a new user with read only 
-- privileges for said database.
CREATE DATABASE IF NOT EXIST hbtn_0d_2;
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT READ PRVILEGES ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;