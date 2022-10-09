/*Criação de tabelas*/

CREATE TABLE IF NOT EXISTS users (
	id int not null GENERATED ALWAYS AS IDENTITY ,
	name varchar(100) not null,
	login varchar(20)not null,
	password varchar(32) not null,
	primary key (id)
);

CREATE TABLE IF NOT EXISTS category_name (
	id int not null GENERATED ALWAYS AS IDENTITY,
	name varchar(250) not null,
	PRIMARY key (id)
);


CREATE TABLE IF NOT EXISTS course (
	id int not null GENERATED ALWAYS AS IDENTITY,
	title varchar(250) not null,
	course_load int not NULL,
	author varchar(150),
	Primary key (id)
);

CREATE TABLE IF NOT EXISTS lesson (
	id int not null GENERATED ALWAYS AS IDENTITY,
	name varchar(150)not null,
	url varchar(1000) not null,
	course_id int not null,
	PRIMARY key (id),
	FOREIGN key (course_id) REFERENCES course(id)
);

CREATE TABLE IF NOT EXISTS category_course (
	course_id int not null,
	category_id int not null,
	FOREIGN key (course_id) REFERENCES course(id),
	FOREIGN key (category_id) REFERENCES category_name(id)
);

CREATE TABLE IF NOT EXISTS registry (
	id int not null GENERATED ALWAYS AS IDENTITY,
	type varchar(50) not null,
	course_id int not null,
	user_id int not null,
	foreign key (user_id) references users(id),
	FOREIGN key (course_id) REFERENCES course(id)
);

CREATE TABLE IF NOT EXISTS review (
	id int not null GENERATED ALWAYS AS IDENTITY,
	grade int not null,
	course_id int not null,
	user_id int not null,
	primary key (id),
	foreign key (user_id) references users(id),
	FOREIGN key (course_id) REFERENCES course(id)
);