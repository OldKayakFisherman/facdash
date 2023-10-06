DROP TABLE census_data.notes;

CREATE TABLE census_data.notes
(
	id serial not null,
	dbkey text,
	audityear text,
    source_id text,
    reportid text,
    version text,
    seq_number  text,
    type_id text,
    note_index text,
    title text,
    content text,
	CONSTRAINT pk_import_notes PRIMARY KEY ("id")
);

ALTER TABLE census_data.notes OWNER TO facdata;
