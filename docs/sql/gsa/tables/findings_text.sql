DROP TABLE gsa_data.findings_text;

CREATE TABLE gsa_data.findings_text
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    finding_ref_number text,
    contains_chart_or_table text,
    finding_text text
);

ALTER TABLE gsa_data.findings_text OWNER TO facdata;


