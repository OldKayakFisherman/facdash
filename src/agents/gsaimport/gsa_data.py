import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import execute_values
from gsa_config import DatabaseSettings
import sys


def convert_boolean(value: str):
    return str(value).lower() in ("yes", "true", "t", "1", "y")


def get_connection():
    try:

        settings = DatabaseSettings()

        db_conn = ThreadedConnectionPool(
            minconn=1,
            maxconn=5,
            user=settings.user,
            database=settings.database,
            host=settings.host,
            port=settings.port,
            options=f'-c search_path={settings.schema}'
        ).getconn()

        return db_conn
    except Exception as e:
        print(e)
        sys.exit(-1)


def get_last_import():
    cn = get_connection()
    cur = cn.cursor()

    sql = """
        SELECT max(fac_accepted_date)
        FROM general
    """

    cur.execute(sql)
    return cur.fetchone()


def save_general_records(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    INSERT INTO general
    (report_id, auditee_uei, audit_year, auditee_certify_name, auditee_certify_title,
    auditee_contact_name, auditee_email, auditee_name, auditee_phone,auditee_contact_title,
    auditee_address_line_1,auditee_city,auditee_state,auditee_ein,auditee_zip,auditor_phone,
    auditor_state,auditor_city,auditor_contact_title,auditor_address_line_1,auditor_zip,
    auditor_country,auditor_contact_name,auditor_email,auditor_firm_name,auditor_foreign_address,
    auditor_ein,cognizant_agency,oversight_agency,date_created,ready_for_certification_date,
    auditor_certified_date,auditee_certified_date,submitted_date,fac_accepted_date,fy_end_date,
    fy_start_date,audit_type,gaap_results,sp_framework_basis,is_sp_framework_required,sp_framework_opinions,
    is_going_concern_included,is_internal_control_deficiency_disclosed,is_internal_control_material_weakness_disclosed,
    is_material_noncompliance_disclosed,dollar_threshold,is_low_risk_auditee,agencies_with_prior_findings,
    entity_type,number_months,audit_period_covered,total_amount_expended,type_audit_code,is_public,
    data_source)
    VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["auditee_certify_name"],
            record["auditee_certify_title"],
            record["auditee_contact_name"],
            record["auditee_email"],
            record["auditee_name"],
            record["auditee_phone"],
            record["auditee_contact_title"],
            record["auditee_address_line_1"],
            record["auditee_city"],
            record["auditee_state"],
            record["auditee_ein"],
            record["auditee_zip"],
            record["auditor_phone"],
            record["auditor_state"],
            record["auditor_city"],
            record["auditor_contact_title"],
            record["auditor_address_line_1"],
            record["auditor_zip"],
            record["auditor_country"],
            record["auditor_contact_name"],
            record["auditor_email"],
            record["auditor_firm_name"],
            record["auditor_foreign_address"],
            record["auditor_ein"],
            record["cognizant_agency"],
            record["oversight_agency"],
            record["date_created"],
            record["ready_for_certification_date"],
            record["auditor_certified_date"],
            record["auditee_certified_date"],
            record["submitted_date"],
            record["fac_accepted_date"],
            record["fy_end_date"],
            record["fy_start_date"],
            record["audit_type"],
            record["gaap_results"],
            record["sp_framework_basis"],
            convert_boolean(record["is_sp_framework_required"]),
            record["sp_framework_opinions"],
            convert_boolean(record["is_going_concern_included"]),
            convert_boolean(record["is_internal_control_deficiency_disclosed"]),
            convert_boolean(record["is_internal_control_material_weakness_disclosed"]),
            convert_boolean(record["is_material_noncompliance_disclosed"]),
            record["dollar_threshold"],
            convert_boolean(record["is_low_risk_auditee"]),
            record["agencies_with_prior_findings"],
            record["entity_type"],
            record["number_months"],
            record["audit_period_covered"],
            record["total_amount_expended"],
            record["type_audit_code"],
            convert_boolean(record["is_public"]),
            record["data_source"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_awards(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO awards
        (report_id,auditee_uei, audit_year, award_reference, federal_agency_prefix,
        federal_award_extension,additional_award_identification,federal_program_name,
        amount_expended,cluster_name,other_cluster_name,state_cluster_name,cluster_total,
        federal_program_total,is_major,is_loan,loan_balance,is_direct,audit_report_type,
        findings_count,is_passthrough_award,passthrough_amount)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["award_reference"],
            record["federal_agency_prefix"],
            record["federal_award_extension"],
            record["additional_award_identification"],
            record["federal_program_name"],
            record["amount_expended"],
            record["cluster_name"],
            record["other_cluster_name"],
            record["state_cluster_name"],
            record["cluster_total"],
            record["federal_program_total"],
            convert_boolean(record["is_major"]),
            convert_boolean(record["is_loan"]),
            record["loan_balance"],
            convert_boolean(record["is_direct"]),
            record["audit_report_type"],
            record["findings_count"],
            convert_boolean(record["is_passthrough_award"]),
            record["passthrough_amount"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_secondary_auditors(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO secondary_auditors
        (auditee_uei,audit_year,auditor_ein,auditor_name,contact_name,
        contact_email,contact_phone,address_street,address_city,address_state,
        address_zipcode)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["auditee_uei"],
            record["audit_year"],
            record["auditor_ein"],
            record["auditor_name"],
            record["contact_name"],
            record["contact_email"],
            record["contact_phone"],
            record["address_street"],
            record["address_city"],
            record["address_state"],
            record["address_zipcode"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_notes_to_sefa(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    INSERT INTO notes_to_sefa
    (report_id,auditee_uei,audit_year,title,accounting_policies,
    is_minimis_rate_used,rate_explained,contains_chart_or_table)
    VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["title"],
            record["accounting_policies"],
            convert_boolean(record["is_minimis_rate_used"]),
            record["rate_explained"],
            convert_boolean(record["contains_chart_or_table"])
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_corrective_action_plans(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO corrective_action_plans
        (report_id,auditee_uei,audit_year,finding_ref_number,
        contains_chart_or_table,planned_action)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["finding_ref_number"],
            record["contains_chart_or_table"],
            record["planned_action"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_findings(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO findings
        (report_id, auditee_uei, audit_year, award_reference, reference_number,
        is_material_weakness, is_modified_opinion, is_other_findings, is_other_matters,
        prior_finding_ref_numbers, is_questioned_costs, is_repeat_finding, is_significant_deficiency,
        type_requirement)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["award_reference"],
            record["reference_number"],
            convert_boolean(record["is_material_weakness"]),
            convert_boolean(record["is_modified_opinion"]),
            convert_boolean(record["is_other_findings"]),
            convert_boolean(record["is_other_matters"]),
            record["prior_finding_ref_numbers"],
            convert_boolean(record["is_questioned_costs"]),
            convert_boolean(record["is_repeat_finding"]),
            convert_boolean(record["is_significant_deficiency"]),
            record["type_requirement"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_passthroughs(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO passthroughs
        (report_id, auditee_uei, audit_year, award_reference,
        passthrough_id, passthrough_name)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["award_reference"],
            record["passthrough_id"],
            record["passthrough_name"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_ueis(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO additional_ueis
        (report_id, auditee_uei, audit_year, additional_uei)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["additional_uei"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()


def save_findings_text(records):

    if not records:
        return

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        INSERT INTO findings_text
        (report_id, auditee_uei, audit_year, finding_ref_number, contains_chart_or_table, 
        finding_text)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append((
            record["report_id"],
            record["auditee_uei"],
            record["audit_year"],
            record["finding_ref_number"],
            record["contains_chart_or_table"],
            record["finding_text"]
        ))

    execute_values(cur, sql, sql_params, template=None, page_size=500)
    cn.commit()
