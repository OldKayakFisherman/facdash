import sys


from psycopg2.pool import ThreadedConnectionPool
from facconfig import DatabaseSettings
from psycopg2.extras import execute_values


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


def clean_import_table(tablename):

    cn = get_connection()
    cur = cn.cursor()

    sql = f"TRUNCATE TABLE census_data.{tablename}"

    cur.execute(sql)

    cn.commit()

def insert_general_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        insert into general (audityear, dbkey, typeofentity, fyenddate, audittype, periodcovered, numbermonths, ein,
        multipleeins, einsubcode, duns, multipleduns, auditeename, street1, street2, city, state, zipcode,
        auditeecontact, auditeetitle, auditeephone, auditeefax, auditeeemail, auditeedatesigned,
        auditeenametitle, cpafirmname, cpastreet1, cpastreet2, cpacity, cpastate, cpazipcode, cpacontact,
        cpatitle, cpaphone, cpafax, cpaemail, cpadatesigned, cog_over, cogagency, oversightagency,
        typereport_fs, sp_framework, sp_framework_required, typereport_sp_framework, goingconcern,
        reportablecondition, materialweakness, materialnoncompliance, typereport_mp, dup_reports,
        dollarthreshold, lowrisk, reportablecondition_mp, materialweakness_mp, qcosts, cyfindings,
        pyschedule, totfedexpend, datefirewall, previousdatefirewall, reportrequired, multiple_cpas,
        auditor_ein, facaccepteddate, cpaforeign, cpacountry, entity_type, uei, multipleueis)
        VALUES %s
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record['audityear'],
                record['dbkey'],
                record['typeofentity'],
                record['fyenddate'],
                record['audittype'],
                record['periodcovered'],
                record['numbermonths'],
                record['ein'],
                record['multipleeins'],
                record['einsubcode'],
                record['duns'],
                record['multipleduns'],
                record['auditeename'],
                record['street1'],
                record['street2'],
                record['city'],
                record['state'],
                record['zipcode'],
                record['auditeecontact'],
                record['auditeetitle'],
                record['auditeephone'],
                record['auditeefax'],
                record['auditeeemail'],
                record['auditeedatesigned'],
                record['auditeenametitle'],
                record['cpafirmname'],
                record['cpastreet1'],
                record['cpastreet2'],
                record['cpacity'],
                record['cpastate'],
                record['cpazipcode'],
                record['cpacontact'],
                record['cpatitle'],
                record['cpaphone'],
                record['cpafax'],
                record['cpaemail'],
                record['cpadatesigned'],
                record['cog_over'],
                record['cogagency'],
                record['oversightagency'],
                record['typereport_fs'],
                record['sp_framework'],
                record['sp_framework_required'],
                record['typereport_sp_framework'],
                record['goingconcern'],
                record['reportablecondition'],
                record['materialweakness'],
                record['materialnoncompliance'],
                record['typereport_mp'],
                record['dup_reports'],
                record['dollarthreshold'],
                record['lowrisk'],
                record['reportablecondition_mp'],
                record['materialweakness_mp'],
                record['qcosts'],
                record['cyfindings'],
                record['pyschedule'],
                record['totfedexpend'],
                record['datefirewall'],
                record['previousdatefirewall'],
                record['reportrequired'],
                record['multiple_cpas'],
                record['auditor_ein'],
                record['facaccepteddate'],
                record['cpaforeign'],
                record['cpacountry'],
                record['entity_type'],
                record['uei'],
                record['multipleueis']
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_cfda_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into cfdas 
    (audityear, dbkey, ein, cfda, awardidentification, rd, federalprogramname, amount, clustername,
    stateclustername, programtotal, clustertotal, direct, passthroughaward, passthroughamount,
    majorprogram, typereport_mp, typerequirement, qcosts2, findings, findingrefnums, arra, loans,
    loanbalance, findingscount, elecauditsid, otherclustername, cfdaprogramname)
    values %s               
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["audityear"],
                record["dbkey"],
                record["ein"],
                record["cfda"],
                record["awardidentification"],
                record["rd"],
                record["federalprogramname"],
                record["amount"],
                record["clustername"],
                record["stateclustername"],
                record["programtotal"],
                record["clustertotal"],
                record["direct"],
                record["passthroughaward"],
                record["passthroughamount"],
                record["majorprogram"],
                record["typereport_mp"],
                record["typerequirement"],
                record["qcosts2"],
                record["findings"],
                record["findingrefnums"],
                record["arra"],
                record["loans"],
                record["loanbalance"],
                record["findingscount"],
                record["elecauditsid"],
                record["otherclustername"],
                record["cfdaprogramname"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()

def insert_finding_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into findings
    (
        dbkey,audityear,elecauditsid,elecauditfindingsid,findingsrefnums,
        typerequirement,modifiedopinion, othernoncompliance,materialweakness,
        significantdeficiency,otherfindings,qcosts,repeatfinding,priorfindingrefnums
    )
    values %s   
    """


    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["dbkey"],
                record["audityear"],
                record["elecauditsid"],
                record["elecauditfindingsid"],
                record["findingsrefnums"],
                record["typerequirement"],
                record["modifiedopinion"],
                record["othernoncompliance"],
                record["materialweakness"],
                record["significantdeficiency"],
                record["otherfindings"],
                record["qcosts"],
                record["repeatfinding"],
                record["priorfindingrefnums"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_cpa_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into cpas
    (
        dbkey,audityear,cpafirmname,cpaein,cpastreet1,cpacity,cpastate,
        cpazipcode,cpacontact,cpatitle,cpaphone,cpafax,cpaemail
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["dbkey"],
                record["audityear"],
                record["cpafirmname"],
                record["cpaein"],
                record["cpastreet1"],
                record["cpacity"],
                record["cpastate"],
                record["cpazipcode"],
                record["cpacontact"],
                record["cpatitle"],
                record["cpaphone"],
                record["cpafax"],
                record["cpaemail"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_agency_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into agencies
    (
        audityear, dbkey, ein, agency
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["audityear"],
                record["dbkey"],
                record["ein"],
                record["agency"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()

def insert_ein_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into eins
    (
        audityear, dbkey, ein, einseqnum
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["audityear"],
                record["dbkey"],
                record["ein"],
                record["einseqnum"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()

def insert_dun_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into duns
    (
        audityear, dbkey, duns, dunseqnum
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["audityear"],
                record["dbkey"],
                record["duns"],
                record["dunseqnum"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_captext_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into captext
    (
        seq_number, dbkey, audityear, findingrefnums,
        text,chartstables
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["seq_number"],
                record["dbkey"],
                record["audityear"],
                record["findingrefnums"],
                record["text"],
                record["chartstables"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()

def insert_findingstext_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into findingstext
    (
        seq_number, dbkey, audityear, findingrefnums,
        text,chartstables
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["seq_number"],
                record["dbkey"],
                record["audityear"],
                record["findingrefnums"],
                record["text"],
                record["chartstables"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_notes_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into notes
    (
        source_id, reportid, version, audityear,
        dbkey, seq_number, type_id, note_index,
        title, content
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["source_id"],
                record["reportid"],
                record["version"],
                record["audityear"],
                record["dbkey"],
                record["seq_number"],
                record["type_id"],
                record["note_index"],
                record["title"],
                record["content"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_passthrough_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into passthrough
    (
        dbkey,audityear,elecauditsid,
        passthroughname,passthroughid
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["dbkey"],
                record["audityear"],
                record["elecauditsid"],
                record["passthroughname"],
                record["passthroughid"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()

def insert_revision_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into revisions
    (
        dbkey,audityear,geninfo,geninfo_explain,federalawards,
        federalawards_explain,notestosefa,notestosefa_explain,
        auditinfo,auditinfo_explain,findings,findings_explain,
        findingstext,findingstext_explain,cap,cap_explain,
        other,other_explain,elecrptrevisionid
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["dbkey"],
                record["audityear"],
                record["geninfo"],
                record["geninfo_explain"],
                record["federalawards"],
                record["federalawards_explain"],
                record["notestosefa"],
                record["notestosefa_explain"],
                record["auditinfo"],
                record["auditinfo_explain"],
                record["findings"],
                record["findings_explain"],
                record["findingstext"],
                record["findingstext_explain"],
                record["cap"],
                record["cap_explain"],
                record["other"],
                record["other_explain"],
                record["elecrptrevisionid"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()


def insert_uei_records(records):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
    insert into ueis
    (
        audityear,dbkey,uei,ueiseqnum
    )
    values %s   
    """

    sql_params = []

    for record in records:
        sql_params.append(
            (
                record["dbkey"],
                record["audityear"],
                record["uei"],
                record["ueiseqnum"]
            )
        )

    execute_values(cur, sql, sql_params, template=None, page_size=500)

    cn.commit()

