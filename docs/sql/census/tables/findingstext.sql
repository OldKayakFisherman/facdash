DROP TABLE census_data.findingstext;

CREATE TABLE census_data.findingstext
(
	id serial not null,
	seq_number text,
	dbkey text,
	audityear text,
	findingrefnums text,
	text text,
	chartstables text,
	CONSTRAINT pk_import_findingstext PRIMARY KEY ("id")
);

ALTER TABLE census_data.findingstext OWNER TO facdata;
