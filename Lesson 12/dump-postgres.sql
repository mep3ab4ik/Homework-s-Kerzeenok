--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-04-21 19:45:02

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

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3345 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 17344)
-- Name: comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    text text NOT NULL,
    user_id integer,
    post_id integer
);


ALTER TABLE public.comments OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 17343)
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 17362)
-- Name: likes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer,
    post_id integer
);


ALTER TABLE public.likes OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17361)
-- Name: likes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 213 (class 1259 OID 17331)
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title text,
    description text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 17330)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 17323)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name text NOT NULL,
    age integer NOT NULL,
    gender text NOT NULL,
    nationality text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 17322)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
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
-- TOC entry 3337 (class 0 OID 17344)
-- Dependencies: 215
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (1, 'lalala', 1, 5);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (2, 'blabla', 2, 1);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (3, 'lilili', 3, 5);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (4, 'kurlak', 1, 2);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (5, 'gnomiki', 4, 5);


--
-- TOC entry 3339 (class 0 OID 17362)
-- Dependencies: 217
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (1, 4, 1);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (2, 2, 3);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (3, 4, 2);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (4, 4, 5);


--
-- TOC entry 3335 (class 0 OID 17331)
-- Dependencies: 213
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (1, 'Hi', 'sql', 1);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (2, 'Hi1', 'sql1', 3);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (3, 'Hi2', 'sql2 ', 2);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (4, 'Hi3', 'sql3', 4);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (5, 'Hi4', 'sql4', 5);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (6, 'Hi5', 'sql5', 1);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (7, 'Hi6', 'sql6', 4);


--
-- TOC entry 3333 (class 0 OID 17323)
-- Dependencies: 211
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (1, 'Andrei', 14, 'm', 'R');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (2, 'Grigorii', 20, 'm', 'R');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (3, 'Kirill', 19, 'm', 'S');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (4, 'Fedor', 40, 'm', 'S');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (5, 'Vikor', 90, 'm', 'U');


--
-- TOC entry 3346 (class 0 OID 0)
-- Dependencies: 214
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.comments_id_seq', 5, true);


--
-- TOC entry 3347 (class 0 OID 0)
-- Dependencies: 216
-- Name: likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.likes_id_seq', 4, true);


--
-- TOC entry 3348 (class 0 OID 0)
-- Dependencies: 212
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 7, true);


--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 210
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- TOC entry 3185 (class 2606 OID 17350)
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- TOC entry 3187 (class 2606 OID 17366)
-- Name: likes likes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pkey PRIMARY KEY (id);


--
-- TOC entry 3183 (class 2606 OID 17337)
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- TOC entry 3181 (class 2606 OID 17329)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3190 (class 2606 OID 17356)
-- Name: comments comments_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 3189 (class 2606 OID 17351)
-- Name: comments comments_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3192 (class 2606 OID 17372)
-- Name: likes likes_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 3191 (class 2606 OID 17367)
-- Name: likes likes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3188 (class 2606 OID 17338)
-- Name: posts posts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


-- Completed on 2022-04-21 19:45:03

--
-- PostgreSQL database dump complete
--

