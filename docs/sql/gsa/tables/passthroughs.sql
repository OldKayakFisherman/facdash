DROP TABLE gsa_data.passthroughs;

CREATE TABLE gsa_data.passthroughs
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    award_reference text,
    passthrough_id text,
    passthrough_name text
);

ALTER TABLE gsa_data.passthroughs OWNER TO facdata;


