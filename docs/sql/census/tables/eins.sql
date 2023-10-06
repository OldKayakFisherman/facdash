DROP TABLE census_data.eins;

CREATE TABLE census_data.eins
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	ein varchar(9),
	einseqnum varchar(4),
	CONSTRAINT pk_import_eins PRIMARY KEY ("id")
);

ALTER TABLE census_data.eins OWNER TO facdata;
