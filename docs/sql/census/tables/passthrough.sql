DROP TABLE TABLE census_data.passthrough;

CREATE TABLE census_data.passthrough
(
	id serial not null,
	dbkey text,
	audityear text,
	elecauditsid text,
	passthroughname text,
	passthroughid text,
	CONSTRAINT pk_import_passthrough PRIMARY KEY ("id")
);

ALTER TABLE census_data.passthrough OWNER TO facdata;
