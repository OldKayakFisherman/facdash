DROP TABLE gsa_data.awards;

CREATE TABLE gsa_data.awards
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    award_reference text,
    federal_agency_prefix text,
    federal_award_extension text,
    additional_award_identification text,
    federal_program_name text,
    amount_expended text,
    cluster_name text,
    other_cluster_name text,
    state_cluster_name text,
    cluster_total money,
    federal_program_total money,
    is_major bool,
    is_loan bool,
    loan_balance text,
    is_direct bool,
    audit_report_type text,
    findings_count int,
    is_passthrough_award bool,
    passthrough_amount money

);

ALTER TABLE gsa_data.awards OWNER TO facdata;


