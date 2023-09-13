CREATE DATABASE chat-app-db;
use chat-app-db;

CREATE TABLE rooms (
  ID int NOT NULL,
  name varchar(255) NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE users (
  ID int NOT NULL,
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

