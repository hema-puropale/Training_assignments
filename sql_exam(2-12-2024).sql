-- CREATE database MYPROJECTS;
create database MyProjects;
show databases;

use MyProjects;

--  Task 1: Creating Table Employee1
create table Employee1(id int primary key not null auto_increment,name char(30),salary int);
show tables;

--  Task 2: Inserting Data into Employee1 table
insert into Employee1(name,Salary) values('hema',80000),('ranjith',100000),('amulya',50000),('archana',20000),('gouthami',30000),('shailaja',40000),('ram',45000),
('sita',44000),('purple',46000);
select * from Employee1;

--  Task 3: Select with WHERE 
select name,salary from Employee1 where salary>50000;

-- Task 4: Select with AND 
select name,salary from Employee1 where salary>40000 and salary<60000;

--  Task 5: Select with NOT 
select name,salary from Employee1 where not salary=55000;

-- Task 6: Order By
select * from Employee1 order by salary desc;

--  Task 7: Select with OR
select * from Employee1 where salary<45000 or salary>60000;

