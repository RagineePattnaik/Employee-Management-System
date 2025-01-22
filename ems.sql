create database ems;
use ems;
create table employees(employee_id varchar(255),employee_name varchar(255),company_name varchar(255),employee_email varchar(255),employee_pswd varchar(255));
insert into employees values("003","Ren","Saintgobain","er@.com","125");
select * from employees;
update employees set employee_name="Waqer" where employee_id="001";
create table pos(pos_id varchar(255),pos_name varchar(255));
insert into pos values("013","Analyst");
select * from pos;
create table manager(manager_name varchar(255),employee_name varchar(255));
insert into manager values("Ritu","Ema");
select * from manager;
create table deprt(dept_name varchar(255),dept_id varchar(255),employee_name varchar(255),salary_pm varchar(255));
insert into deprt values("Management","087","Ren","95000");
select * from deprt;
create table present(employee_id varchar(255),no_of_days_present varchar(255));
insert into present values("003","316");
select * from present;
create table up(employee_id varchar(255),dept_id varchar(255),joining_date varchar(255));
insert into up values("003","087","2021-07-08 3:20:20");
select * from up;


