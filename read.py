from util import get_connection

def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_connection(db_type='mysql',
                                db_host=SOURCE_DB['DB_HOST'],
                                db_user=SOURCE_DB['DB_USER'],
                                db_pass=SOURCE_DB['DB_PASS'],
                                db_name=SOURCE_DB['DB_NAME'])
    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names
    connection.close()
    return data, column_names