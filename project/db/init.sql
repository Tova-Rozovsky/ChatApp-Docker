CREATE DATABASE chat;
use chat;







CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT PRIMARY KEY (Personid),
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

CREATE TABLE users (
  ID int NOT NULL AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  password varchar NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE msg (
  ID int NOT NULL,
  msg varchar(255) NOT NULL,
  room int FOREIGN KEY REFERENCES rooms(ID)
  user int FOREIGN KEY REFERENCES users(ID)
  PRIMARY KEY (ID)
);

