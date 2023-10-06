DROP TABLE census_data.duns;

CREATE TABLE census_data.duns
(
	id serial not null,
	audityear varchar(4),
	dbkey varchar(10),
	duns varchar(9),
	dunseqnum varchar(4),
	CONSTRAINT pk_import_duns PRIMARY KEY ("id")
);

ALTER TABLE census_data.duns OWNER TO facdata;
