use hema;
create table users(id int not null primary key auto_increment, userName varchar(30));
show tables;
delete from users where id is NULL;
insert into users(userName) values('Hema'),('Ranjith'),('Amulya'),('Shailaja');
select * from users;
create table orders(order_id int not null primary key auto_increment,cost int(30),user_id int,foreign key(user_id) references users(id) on delete cascade);
select * from orders;
insert into orders(user_id,cost) values('4','350');
select userName,count(*) from users join orders on orders.user_id=users.id group by userName;

-- task 2
create table students(id int not null primary key auto_increment, name varchar(30));
insert into students(name) values('d');
select * from students;
create table courses (course_id int not null primary key auto_increment,course_name varchar(30));
insert into courses(course_name) values('Biology');
select * from courses;
create table enrollments(student_id int,course_id int,foreign key(course_id) references courses(course_id));
select * from enrollments;
insert into enrollments(student_id,course_id) values('4','3');

select students.Name as student_name, courses.course_name as courseEnrolled
from students
join enrollments ON enrollments.student_id = students.id
join courses ON enrollments.course_id = courses.course_id;

-- task 3
select category, sum(price) from products group by category;

-- task 4
alter table employees add manager varchar (30);
select * from employees;
update employees set manager='anuhya';
update employees set manager='Durga' where employee_id in (1,2,5,8); 
select employee_name, manager from employees;

-- task 5
alter table products add unitsSold int;
update products set unitsSold='5' where product_id="1";
update products set unitsSold='1' where product_id="2";
update products set unitsSold='4' where product_id="3";
update products set unitsSold='4' where product_id="4";
update products set unitsSold='2' where product_id="5";
update products set unitsSold='1' where product_id="6";
update products set unitsSold='2' where product_id="7";
update products set unitsSold='2' where product_id="8";
update products set unitsSold='2' where product_id="9";
update products set unitsSold='1' where product_id="10";
select product_name,unitsSold from products order by unitsSold desc limit 10;

-- task 6
select * from students;
select * from courses;
create table grades (student_id int, course_id int, grade int);
insert into grades values ('1','1','10'), ('1','2','10'), ('1','3','9'), ('1','4','8'), ('2','1','8'), ('2','2','10'), ('2','3','10'), ('2','4','7'),
('3','1','10'), ('3','2','10'), ('3','3','9'), ('3','4','5'), ('4','1','6'), ('4','2','10'), ('4','3','5'), ('4','4','6');
select * from grades;
select students.name, AVG (grades.grade)as avg_grade from grades join courses on courses.course_id=grades.course_id join students on students.id=grades.student_id group by students.name;

-- task 7
create table socialMedia (id int primary key not null auto_increment,name varchar(30),friends int);
insert into socialMedia (name,friends) values('hema',500),('sandhya',200),('ranjith',1000),('raj',50),('meo',60);
select name, friends from socialMedia where friends>100 order by friends desc;

-- task 8
create table departments (id int primary key not null auto_increment,department_name varchar(30));
insert into departments(department_name) values ('cse'),('ece');
select * from departments;
alter table employees add department_id int, add constraint fk_department foreign key(department_id) references departments(id);
update employees set department_id=1;
update employees set department_id=2 where employee_id in (2,5,6,8);
select * from employees;
select department_name,count(*) as no_of_employees from departments join employees on departments.id=employees.department_id group by employees.department_id;

-- task 9
update clothing set In_stock='No' where cloth_id in (4,6);
select cloth_id, cloth_name from clothing where In_stock='No';

-- task 10
select userName, Avg(cost) from orders join users on users.id=orders.user_id group by orders.user_id;

-- task 11
create table ratings (id int not null primary key auto_increment, movie_name varchar(30),rating int,
user_id int,foreign key(user_id) references users(id));
insert into ratings(movie_name, rating,user_id) values('Bahubali',10,1),('Patas',9,2),('Mr Perfect',9,3),('Agadu',4,4),('100% Love',8,5),('RRR',10,2);
select userName,movie_name,rating from ratings join users on ratings.user_id=users.id order by rating desc limit 5;

-- task 12
create table invoices (invoice_id int primary key not null auto_increment,Total_amount int);
insert into invoices (Total_amount) values (100),(400),(600),(400),(250),(350);
create table payments (user_id int,invoice_id int,foreign key(invoice_id) references invoices(invoice_id), payment_status varchar(20));
insert into payments values(1,1,'No'), (1,2,'Yes'), (2,3,'No'), (3,4,'No'), (3,5,'No'), (4,6,'yes');
select user_id, invoices.invoice_id, payment_status, Total_amount from payments join invoices on payments.invoice_id=invoices.invoice_id where payment_status='No';






