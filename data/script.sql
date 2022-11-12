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
	description varchar not null,
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
	course(author_id,course_load,title,description)
VALUES
	(1,'500','Banco de Dados - MySQL','Descrição do curso!'),
	(1,'500','Excel 2016','Descrição do curso!'),
	(2,'500','Curso de Programação em Linguagem C','Descrição do curso!'),
	(1,'500','JavaScript','Descrição do curso!'),
	(3,'500','Curso Trello básico ','Descrição do curso!');

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
	lesson(course_id,name,video_uuid)
VALUES
	(1,'#1 - O que é um Banco de Dados?','966f23ab-776a-43f6-b43e-aca031c70cd2'),
	(1,'#2A - Instalando o MySQL com WAMP','e004b0f3-97f6-41db-9274-e32c3e582bca'),
	(1,'#2B - Instalando o XAMPP','eb11de2d-e47a-49e3-9ee3-2569abf022b1'),
	(1,'#3 - Criando o primeiro Banco de Dados','1f8d6695-dba3-4f87-9358-40731194ae1a'),
	(1,'#4 - Melhorando a Estrutura do Banco de Dados','2b5d316a-071a-4ea6-8238-bfa276b4b7be'),
	(1,'#5 - Inserindo Dados na Tabela','5fff4c44-6c41-40f7-b461-c36202de9b9e'),
	(2,'1º - Surgimento do Excel','9abfc16e-a7a1-489d-bc1e-21d397866c57'),
	(2,'2º - 10 Dicas e Truques com Excel','064ceb49-347b-4806-b17a-3bc527fe8f2e'),
	(2,'3º - Primeiros Passos no Excel','0174f580-9346-4095-af14-db1490abc4fd'),
	(2,'4º - Manipulação de Arquivos','877379fd-0f92-4c6a-8ba0-6397995881ad'),
	(2,'5º - Selecionando Dados','5befd4bc-e9d6-462d-9afc-14a23fff636b');
