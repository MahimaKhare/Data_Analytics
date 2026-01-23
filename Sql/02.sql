Create Database Restaurant;
Use Restaurant;

CREATE TABLE person (
    PID INT PRIMARY KEY,
    Name VARCHAR(50),
    Address VARCHAR(100)
);

-- Alter
-- 01. Add coloumn 
Alter Table person
Add last_name varchar(50);

-- 02. Modify
Alter Table person
add last_name char;  

-- 03. Rename
Alter Table person
rename column last_name to l_name;  

-- 04. drop
Alter Table person 
Drop l_name;

-- Constraints
use restaurant;

Create Table orders( 
    OID INT PRIMARY KEY,
    OrderName VARCHAR(50) not null,
    PID INT Not null unique auto_increment,
    Age Int check(age >= 18),
    City Varchar(20) default 'Sikar',
    FOREIGN KEY(PID) REFERENCES person(PID)
);
use restaurant


Select * from person;
Select * from orders;





   
    