DROP TABLE TABLE census_data.ueis;

CREATE TABLE census_data.ueis
(
	id serial not null,
    dbkey text,
    audityear text,
    uei text,
    ueiseqnum text,
	CONSTRAINT pk_import_ueis PRIMARY KEY ("id")
);

ALTER TABLE census_data.ueis OWNER TO facdata;