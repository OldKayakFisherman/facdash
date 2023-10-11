CREATE OR REPLACE VIEW vw_export_processing_queue
AS

   SELECT
    'CEN' || dbkey || '-' || audityear as report_id,
    CAST(general.audityear AS SMALLINT) as audit_year,
    general.dbkey as dbkey,
    general.auditeename as auditee_name,
    general.street1 as street,
    general.city as city,
    general.state as state,
    general.zipcode as zipcode,
    case general.cyfindings when 'Y' then 50 else 60 end as sflag,
    CAST(facaccepteddate as DATE) as date_received,
    general.ein as ein
    FROM census_data.general
    WHERE census_data.general.audityear > '2015'


UNION

    SELECT
        gsa_data.general.report_id as report_id,
        gsa_data.general.audit_year as audit_year,
        null as dbkey,
        gsa_data.general.auditee_name as auditee_name,
        gsa_data.general.auditor_address_line_1 as street,
        gsa_data.general.auditee_city as city,
        gsa_data.general.auditee_state as state,
        gsa_data.general.auditee_zip as zip,
        null as sflag,
        gsa_data.general.submitted_date  as date_received,
        gsa_data.general.auditee_ein as ein
    from gsa_data.general;

