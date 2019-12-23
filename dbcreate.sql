-- create db
create database datarep;

-- create table
use datarep;
create table products(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(250),
    type varchar(250),
    size int,
    price int,
    PRIMARY KEY(id)
    );

-- insert row of data
INSERT INTO products(name, type, size, price) 
VALUES (Yog Nog, Shower Gel, 250, 2000);