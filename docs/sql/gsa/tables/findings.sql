DROP TABLE gsa_data.findings;

CREATE TABLE gsa_data.findings
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    award_reference text,
    reference_number text,
    is_material_weakness bool,
    is_modified_opinion bool,
    is_other_findings bool,
    is_other_matters bool,
    prior_finding_ref_numbers text,
    is_questioned_costs bool,
    is_repeat_finding bool,
    is_significant_deficiency bool,
    type_requirement text
);

ALTER TABLE gsa_data.findings OWNER TO facdata;


