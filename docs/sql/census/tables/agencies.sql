DROP TABLE census_data.agencies;

CREATE TABLE census_data.agencies
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	ein varchar(9),
	agency varchar(200),
	CONSTRAINT pk_import_agencies PRIMARY KEY ("id")
);

ALTER TABLE census_data.agencies OWNER TO facdata;


