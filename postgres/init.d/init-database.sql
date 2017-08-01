--CREATE DATABASE postgres;

\connect chameleon

--CREATE SCHEMA chemeleon;
--SET search_path = chameleon;

CREATE TABLE mytable (
	    id integer NOT NULL,
	    email character varying(75) NOT NULL,
	    order_date timestamp without time zone NOT NULL,
	    order_source character varying(20) NOT NULL,
	    product_opts jsonb
);

INSERT INTO mytable (id,email,order_date,order_source) VALUES
	(1,'sit.amet.nulla@purus.com','2016-08-15 00:10:39','yellow'),
	(2,'eu.tellus@sitamet.net','2016-09-29 15:41:04','blue'),
	(3,'vulputate@acturpis.co.uk','2017-02-18 15:20:53','yellow'),
	(4,'justo.faucibus@maurisMorbinon.com','2017-06-26 04:54:20','violet'),
	(5,'habitant@tinciduntaliquam.ca','2018-04-22 13:01:14','yellow'),
	(6,'eu.ligula@aliquet.net','2016-09-18 21:37:05','violet'),
	(7,'Phasellus.vitae.mauris@Cras.net','2017-07-19 10:24:43','blue'),
	(8,'sit.amet@vulputateeuodio.org','2016-09-15 08:41:52','orange'),
	(9,'Quisque@sedorci.org','2016-07-29 08:59:58','orange'),
	(10,'eget@tristiquepellentesquetellus.edu','2017-06-07 23:54:29','blue');

