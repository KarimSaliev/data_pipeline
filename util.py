import pandas as pd
from config import DB_DETAILS
from mysql import connector as mc
from mysql.connector import errorcode as ec
import psycopg2
def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    # returns positive records
    return tables.query("to_be_loaded == 'yes'")

def get_mysql_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                database=db_name)
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
        else:
            print(error)

    return connection

def get_pg_connection(db_host, db_name, db_user, db_pass):
    connection = psycopg2.connect(f"dbname={db_name} user={db_user} host={db_host} password={db_pass}")
    return connection
def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type=='mysql':
        connection = get_mysql_connection(db_host=db_host,
                                         db_user=db_user,
                                         db_pass=db_pass,
                                         db_name=db_name)

    elif db_type=='postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_pass=db_pass,)


    return connection

def load_db_details(env):
    return DB_DETAILS[env]