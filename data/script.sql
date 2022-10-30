/*Criação de tabelas*/

CREATE TABLE IF NOT EXISTS users (
	id int not null GENERATED ALWAYS AS IDENTITY ,
	name varchar(100) not null,
	login varchar(100)not null,
	password varchar not null,
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
	author_id int not null,
	Primary key (id),
	FOREIGN key (author_id) references users(id)

);

CREATE TABLE IF NOT EXISTS lesson (
	id int not null GENERATED ALWAYS AS IDENTITY,
	name varchar(150)not null,
	video_uuid varchar(36) not null,
	course_id int not null,
	PRIMARY key (id),
	FOREIGN key (course_id) REFERENCES course(id)
);

CREATE TABLE IF NOT EXISTS category_course (
	course_id int not null,
	category_id int not null,
	FOREIGN key (course_id) REFERENCES course(id),
	FOREIGN key (category_id) REFERENCES category_name(id),
	PRIMARY KEY (course_id, category_id)
);

CREATE TABLE IF NOT EXISTS registry (
	id int not null GENERATED ALWAYS AS IDENTITY,
	is_teacher BOOLEAN not null,
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

/*canais*/
insert into
	users (name,login,password)
values
	('curso em video','cursoemvideo@exemple.com','12345678'),
	('Boson Treinamemtos','boson@exemple.com.br','12345678'),
	('canal valor','valor@exmple.como.br','12345678');

/*categorias*/
insert into
	category_name ("name")
values
	('Banco de dados'),
	('dev'),
	('programção'),
	('excel'),
	('office'),
	('organização'),
	('automação');

/*cursos*/
insert into
	course(author_id,course_load,title)
VALUES
	(1,'500','Banco de Dados - MySQL'),
	(1,'500','Excel 2016'),
	(2,'500','Curso de Programação em Linguagem C'),
	(1,'500','JavaScript'),
	(3,'500','Curso Trello básico ');

/*dando categoria aos cursos*/
insert INTO
	category_course (course_id,category_id)
VALUES
	(1,1),
	(1,2),
	(1,3),
	(2,7),
	(2,4),
	(2,5),
	(3,2),
	(3,3),
	(5,6),
	(5,7);

/*aulas*/
insert into
	lesson(course_id,name,url)
VALUES
	(1,'#1 - O que é um Banco de Dados?','https://www.youtube.com/watch?v=Ofktsne-utM&list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r&index=1'),
	(1,'#2A - Instalando o MySQL com WAMP','https://www.youtube.com/watch?v=5JbAOWJbgIA&list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r&index=2'),
	(1,'#2B - Instalando o XAMPP','https://www.youtube.com/watch?v=R2HrwSQ6EPM&list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r&index=3'),
	(1,'#3 - Criando o primeiro Banco de Dados','https://www.youtube.com/watch?v=m9YPlX0fcJk&list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r&index=4'),
	(1,'#4 - Melhorando a Estrutura do Banco de Dados','https://www.youtube.com/watch?v=cHLKtALWDos&list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r&index=5'),
	(1,'#5 - Inserindo Dados na Tabela','https://www.youtube.com/watch?v=NCG9niOlm40&list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r&index=7'),
	(2,'1º - Surgimento do Excel','https://www.youtube.com/watch?v=ZVURQLXZtIc&list=PLHz_AreHm4dkRZoc0-i4sQeot_62qKi4a&index=1'),
	(2,'2º - 10 Dicas e Truques com Excel','https://www.youtube.com/watch?v=yCRUWtDcrJQ&list=PLHz_AreHm4dkRZoc0-i4sQeot_62qKi4a&index=2'),
	(2,'3º - Primeiros Passos no Excel','https://www.youtube.com/watch?v=X4RLqvl0Ch8&list=PLHz_AreHm4dkRZoc0-i4sQeot_62qKi4a&index=4'),
	(2,'4º - Manipulação de Arquivos','https://www.youtube.com/watch?v=4dBE45hiDz8&list=PLHz_AreHm4dkRZoc0-i4sQeot_62qKi4a&index=5'),
	(2,'5º - Selecionando Dados','https://www.youtube.com/watch?v=ZPQIm6_0Z5A&list=PLHz_AreHm4dkRZoc0-i4sQeot_62qKi4a&index=6');
