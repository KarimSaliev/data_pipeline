import sys
from config import DB_DETAILS
from read import read_table
from util import get_tables, load_db_details
from write import build_insert_query, load_table

def main():
    # Program takes at least one argument
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('table_list.txt')
    for table_name in tables['table_name']:
        print(f"Reading Source DB data for {table_name}...")
        data, column_names = read_table(db_details, table_name)
        print(data, column_names)
        print(f"Loading data for {table_name}...")
        load_table(db_details, data, column_names, table_name)

    print(f"Data loaded for the following tables: {tables}")









if __name__ == '__main__':
    main()