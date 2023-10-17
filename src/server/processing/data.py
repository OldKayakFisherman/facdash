import sys

from psycopg2.extensions import connection, cursor
from psycopg2.pool import ThreadedConnectionPool
from config import DatabaseSettings
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


def get_processing_queue():

    result = []

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        SELECT 
            report_id,audit_year,dbkey,auditee_name,
            city,state,sflag,date_received
        FROM processing.processing_queue
        WHERE dbkey IS NULL
    """
    cur.execute(sql)

    records = cur.fetchall()

    for record in records:
        result.append(
            {
                "report_id": record[0],
                "audit_year": record[1],
                "dbkey": record[2],
                "auditee_name": record[3],
                "city": record[4],
                "state": record[5],
                "sflag": record[6],
                "date_received": record[7]
            }
        )

    return result

def get_workflow_record(report_id: str):

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        SELECT 
            report_id, audit_year, dbkey, auditee_name,
            street, city, state, zipcode, sflag,
            date_received, ein
        FROM processing.processing_queue
        WHERE report_id = %s
    """

    sql_params = (report_id,)

    cur.execute(sql, sql_params)

    row = cur.fetchone()

    if row:
        return {
            "report_id": row[0],
            "audit_year": row[1],
            "dbkey": row[2],
            "auditee_name":row[3],
            "street": row[4],
            "city": row[5],
            "state": row[6],
            "zipcode": row[7],
            "sflag": row[8],
            "date_received": row[9],
            "ein": row[10]
        }

    return None


def get_ein_search(ein: str):

    result = []

    cn = get_connection()
    cur = cn.cursor()

    sql = """
        SELECT 
            audit_year,dbkey,ein,
            auditee_name,report_id
        FROM processing.processing_queue
        WHERE ein = %s
    """
    cur.execute(sql)

    records = cur.fetchall()

    for record in records:
        result.append(
            {
                "audit_year": record[0],
                "dbkey": record[1],
                "ein": record[2],
                "auditee_name": record[3],
                "report_id": record[4]
            }
        )

    return result
