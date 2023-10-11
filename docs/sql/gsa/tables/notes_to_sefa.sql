DROP TABLE gsa_data.notes_to_sefa;

CREATE TABLE gsa_data.notes_to_sefa
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    title text,
    accounting_policies text,
    is_minimis_rate_used bool,
    rate_explained text,
    contains_chart_or_table bool
);

ALTER TABLE gsa_data.notes_to_sefa OWNER TO facdata;


