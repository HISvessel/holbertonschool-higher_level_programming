-- this script creates a new user and grant all privileges to it
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRVILEGES ON *.* TO USER 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;