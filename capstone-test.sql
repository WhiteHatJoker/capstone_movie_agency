--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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
-- Name: Actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Actor" (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    age integer NOT NULL,
    gender character varying(60) NOT NULL,
    city character varying(120) NOT NULL,
    state character varying(120) NOT NULL,
    phone character varying(120) NOT NULL,
    email character varying(120),
    website character varying(120)
);


ALTER TABLE public."Actor" OWNER TO postgres;

--
-- Name: Actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actor_id_seq" OWNER TO postgres;

--
-- Name: Actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Actor_id_seq" OWNED BY public."Actor".id;


--
-- Name: Movie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Movie" (
    id integer NOT NULL,
    title character varying(120) NOT NULL,
    excerpt character varying(500),
    release_date date NOT NULL
);


ALTER TABLE public."Movie" OWNER TO postgres;

--
-- Name: MovieCast; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MovieCast" (
    id integer NOT NULL,
    movie_id integer NOT NULL,
    actor_id integer NOT NULL
);


ALTER TABLE public."MovieCast" OWNER TO postgres;

--
-- Name: MovieCast_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."MovieCast_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."MovieCast_id_seq" OWNER TO postgres;

--
-- Name: MovieCast_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."MovieCast_id_seq" OWNED BY public."MovieCast".id;


--
-- Name: Movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_id_seq" OWNER TO postgres;

--
-- Name: Movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Movie_id_seq" OWNED BY public."Movie".id;


--
-- Name: Actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actor" ALTER COLUMN id SET DEFAULT nextval('public."Actor_id_seq"'::regclass);


--
-- Name: Movie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movie" ALTER COLUMN id SET DEFAULT nextval('public."Movie_id_seq"'::regclass);


--
-- Name: MovieCast id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MovieCast" ALTER COLUMN id SET DEFAULT nextval('public."MovieCast_id_seq"'::regclass);


--
-- Data for Name: Actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Actor" (id, name, age, gender, city, state, phone, email, website) FROM stdin;
1	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
2	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
3	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
4	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
5	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
6	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
7	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
8	Sylvester Stallone	59	Male	Arizona	TX	123456	sylvie@gmail.com	sylvie.com
\.


--
-- Data for Name: Movie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Movie" (id, title, excerpt, release_date) FROM stdin;
1	Dark Knight	See the famous Dark Knight in action	2020-10-08
2	Dark Knight	See the famous Dark Knight in action	2020-10-08
3	Dark Knight	See the famous Dark Knight in action	2020-10-08
4	Dark Knight	See the famous Dark Knight in action	2020-10-08
5	Dark Knight	See the famous Dark Knight in action	2020-10-08
6	Dark Knight and Joker	\N	2020-10-08
\.


--
-- Data for Name: MovieCast; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."MovieCast" (id, movie_id, actor_id) FROM stdin;
\.


--
-- Name: Actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Actor_id_seq"', 14, true);


--
-- Name: MovieCast_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."MovieCast_id_seq"', 6, true);


--
-- Name: Movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Movie_id_seq"', 12, true);


--
-- Name: Actor Actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_pkey" PRIMARY KEY (id);


--
-- Name: MovieCast MovieCast_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MovieCast"
    ADD CONSTRAINT "MovieCast_pkey" PRIMARY KEY (id, movie_id, actor_id);


--
-- Name: Movie Movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_pkey" PRIMARY KEY (id);


--
-- Name: MovieCast MovieCast_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MovieCast"
    ADD CONSTRAINT "MovieCast_actor_id_fkey" FOREIGN KEY (actor_id) REFERENCES public."Actor"(id) ON DELETE CASCADE;


--
-- Name: MovieCast MovieCast_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MovieCast"
    ADD CONSTRAINT "MovieCast_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES public."Movie"(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

