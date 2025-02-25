-- create database not_temu_project;
-- grant all privileges on not_temu_project.* to 계정명@'%';
-- 위 코드는 root에서 실행

CREATE DATABASE not_temu_project default CHARACTER SET UTF8;

use not_temu_project;

create table if not exists license(
is_license boolean,
primary key(is_license)
)engine = innodb;

create table if not exists city(
city_id int auto_increment primary key,
city_name varchar(100),
density int,
car_amount int,
license boolean,
license_population int,
population int,
foreign key(license) references license (is_license)
)engine = innodb;

create table if not exists vehicle(
vehicle_id int auto_increment primary key,
vehicle_name varchar(100),
need_license boolean,
foreign key(need_license) references license (is_license)
)engine = innodb;

create table if not exists faq(
faq_id int auto_increment primary key,
vehicle_id int,
company_name varchar(100),
question TEXT,
answer TEXT,
foreign key(vehicle_id) references vehicle (vehicle_id)
)engine = innodb;
