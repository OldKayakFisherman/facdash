import os
from contextlib import contextmanager

from psycopg2.extensions import connection, cursor
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

load_dotenv()

PG_USER = os.getenv("PGUSER")
PG_PASSWORD = os.getenv("PGPASSWORD")
PG_DATABASE = os.getenv("PGDB")
PG_HOST = os.getenv("PGHOST")

database_dsn = dbConnection = f"host='{PG_HOST}' dbname='{PG_DATABASE}' user='{PG_USER}' password='{PG_PASSWORD}'"

# pool define with 10 live connections
connection_pool = SimpleConnectionPool(1, 10, dsn=database_dsn)

@contextmanager
def getcursor():
    con = connection_pool.getconn()
    try:
        yield con.cursor()
    finally:
        connection_pool.putconn(con)

