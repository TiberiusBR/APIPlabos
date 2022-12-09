--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Debian 15.1-1.pgdg110+1)
-- Dumped by pg_dump version 15.1 (Debian 15.1-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: category_course; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.category_course (
    course_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.category_course OWNER TO "user";

--
-- Name: category_name; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.category_name (
    id integer NOT NULL,
    name character varying(250) NOT NULL
);


ALTER TABLE public.category_name OWNER TO "user";

--
-- Name: category_name_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.category_name ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.category_name_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: course; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.course (
    id integer NOT NULL,
    title character varying(250) NOT NULL,
    description character varying NOT NULL,
	image_url character varying,
    course_load integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.course OWNER TO "user";

--
-- Name: course_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.course ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.course_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: lesson; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.lesson (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    video_uuid character varying(36) NOT NULL,
    course_id integer NOT NULL
);


ALTER TABLE public.lesson OWNER TO "user";

--
-- Name: lesson_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.lesson ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.lesson_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: registry; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.registry (
    id integer NOT NULL,
    is_teacher boolean NOT NULL,
    course_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.registry OWNER TO "user";

--
-- Name: registry_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.registry ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.registry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: review; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.review (
    id integer NOT NULL,
    grade integer NOT NULL,
    course_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.review OWNER TO "user";

--
-- Name: review_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.review ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.review_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    login character varying(100) NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO "user";

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: category_course; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.category_course (course_id, category_id) FROM stdin;
1	1
1	2
1	3
2	7
2	4
2	5
3	2
3	3
5	6
5	7
\.


--
-- Data for Name: category_name; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.category_name (id, name) FROM stdin;
1	Banco de dados
2	dev
3	programção
4	excel
5	office
6	organização
7	automação
\.


--
-- Data for Name: course; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.course (id, title, description, course_load, author_id) FROM stdin;
1	Banco de Dados - MySQL	Descrição do curso!	500	1
2	Excel 2016	Descrição do curso!	500	1
3	Curso de Programação em Linguagem C	Descrição do curso!	500	2
4	JavaScript	Descrição do curso!	500	1
5	Curso Trello básico 	Descrição do curso!	500	3
6	React.js	react do basico ao avancado	44	4
7	Algoritmos e Lógica de Programação	Curso para quem quer começar na programação	15	4
8	Algoritmo e Lógica de Programação	Curso para quem quer começar na programação	15	4
9	teste	teste	50	1
\.

COPY public.course (id, title, description, course_load, author_id, image_url) FROM stdin;
10	teste	Descrição do curso!	500	2	image_path
\.

--
-- Data for Name: lesson; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.lesson (id, name, video_uuid, course_id) FROM stdin;
1	#1 - O que é um Banco de Dados?	966f23ab-776a-43f6-b43e-aca031c70cd2	1
2	#2A - Instalando o MySQL com WAMP	e004b0f3-97f6-41db-9274-e32c3e582bca	1
3	#2B - Instalando o XAMPP	eb11de2d-e47a-49e3-9ee3-2569abf022b1	1
4	#3 - Criando o primeiro Banco de Dados	1f8d6695-dba3-4f87-9358-40731194ae1a	1
5	#4 - Melhorando a Estrutura do Banco de Dados	2b5d316a-071a-4ea6-8238-bfa276b4b7be	1
6	#5 - Inserindo Dados na Tabela	5fff4c44-6c41-40f7-b461-c36202de9b9e	1
7	1º - Surgimento do Excel	9abfc16e-a7a1-489d-bc1e-21d397866c57	2
8	2º - 10 Dicas e Truques com Excel	064ceb49-347b-4806-b17a-3bc527fe8f2e	2
9	3º - Primeiros Passos no Excel	0174f580-9346-4095-af14-db1490abc4fd	2
10	4º - Manipulação de Arquivos	877379fd-0f92-4c6a-8ba0-6397995881ad	2
11	5º - Selecionando Dados	5befd4bc-e9d6-462d-9afc-14a23fff636b	2
12	1. IntroduÃ§Ã£o	5a710808-21b5-434e-9ee3-eb3d56f7c497	7
13	1. Introducao	aee60107-fd69-4046-9ddb-d1239adc5648	8
14	2. O que e algoritmo	becd3133-c252-4eba-bce4-7b51a812b200	8
15	3. Compreendendo logica de programacao	ce74dd1d-960f-48c8-907d-c62615625104	8
\.


--
-- Data for Name: registry; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.registry (id, is_teacher, course_id, user_id) FROM stdin;
1	f	8	5
\.


--
-- Data for Name: review; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.review (id, grade, course_id, user_id) FROM stdin;
1	3	1	1
2	5	1	2
3	2	2	2
4	2	4	1
5	5	4	1
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.users (id, name, login, password) FROM stdin;
1	curso em video	cursoemvideo@exemple.com	12345678
2	Boson Treinamemtos	boson@exemple.com.br	12345678
3	canal valor	valor@exmple.como.br	12345678
4	Kaique Oliveira	kaique.santos@ftc.edu.br	$2b$12$IfuRO75a.uH4K62bdEsEhO5UzsZqvPtSrMJAujKVox8PhfHJR8cre
5	Felipe Freire	felipe.freire@ftc.edu.br	$2b$12$BouxttieuBHZ2TIkJbGltekjf8RLXtRAD1A169/9LvXs.DLXXnPe.
6	Matheus	nodge2	$2b$12$hPzPvpznKUi4Wb41HsqHl.lUTeVJdRtMo.hZOC3JF/XnyZkT9iX/e
7	Matheus	nodge	$2b$12$Ly/yo1E1J/790F3JgWePa.6hoFpUFZ8UPdTTr2LPD3zubbgXeH.lW
8	Matheus	nodge321	$2b$12$tk68mHOgJzjzFC183y7xcuNOcwI9ethU.jQBjFgCvCRinJ0aMVpLm
9	Teste	teste@teste.com	$2b$12$/cQ2TOu3yEu3zeYlSGD09u5GZBPBFjTCl8Pt.XvsbxZqIiMVJi.Gi
10	pinto@pinto.com	123123123	$2b$12$.vnxlbPPwcaJJ7VOUIBDNu7oYlJIlDbHBhlcrVTSm7EpdE7gS9SYC
\.


--
-- Name: category_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.category_name_id_seq', 7, true);


--
-- Name: course_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.course_id_seq', 9, true);


--
-- Name: lesson_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.lesson_id_seq', 15, true);


--
-- Name: registry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.registry_id_seq', 1, true);


--
-- Name: review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.review_id_seq', 5, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.users_id_seq', 10, true);


--
-- Name: category_course category_course_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.category_course
    ADD CONSTRAINT category_course_pkey PRIMARY KEY (course_id, category_id);


--
-- Name: category_name category_name_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.category_name
    ADD CONSTRAINT category_name_pkey PRIMARY KEY (id);


--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (id);


--
-- Name: lesson lesson_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_pkey PRIMARY KEY (id);


--
-- Name: review review_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.review
    ADD CONSTRAINT review_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: category_course category_course_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.category_course
    ADD CONSTRAINT category_course_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category_name(id);


--
-- Name: category_course category_course_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.category_course
    ADD CONSTRAINT category_course_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(id);


--
-- Name: course course_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.users(id);


--
-- Name: lesson lesson_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(id);


--
-- Name: registry registry_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.registry
    ADD CONSTRAINT registry_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(id);


--
-- Name: registry registry_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.registry
    ADD CONSTRAINT registry_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: review review_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.review
    ADD CONSTRAINT review_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.course(id);


--
-- Name: review review_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.review
    ADD CONSTRAINT review_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

