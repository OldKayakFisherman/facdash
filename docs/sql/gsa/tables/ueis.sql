DROP TABLE gsa_data.additional_ueis;

CREATE TABLE gsa_data.additional_ueis
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    additional_uei text
);

ALTER TABLE gsa_data.additional_ueis OWNER TO facdata;


