DROP TABLE gsa_data.secondary_auditors;

CREATE TABLE gsa_data.secondary_auditors
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    auditor_ein text,
    auditor_name text,
    contact_name text,
    contact_email text,
    contact_phone text,
    address_street text,
    address_city text,
    address_state text,
    address_zipcode text
);

ALTER TABLE gsa_data.secondary_auditors OWNER TO facdata;


