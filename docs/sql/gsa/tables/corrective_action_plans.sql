DROP TABLE gsa_data.corrective_action_plans;

CREATE TABLE gsa_data.corrective_action_plans
(
    id serial not null primary key,
    report_id text,
    auditee_uei text,
    audit_year smallint,
    finding_ref_number text,
    contains_chart_or_table bool,
    planned_action text
);

ALTER TABLE gsa_data.corrective_action_plans OWNER TO facdata;


