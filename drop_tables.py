import csv, sqlite3
from sqlite3 import Error
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
def scrub(table_name):
    """ create a table names only in alphanumerics
    scrubing off characters that may be misued for sql injection
    :param table_name: name of the table to create
    :return: name with only alphanumeric characters
    """
    return ''.join( chr for chr in table_name if chr.isalnum() )
    
def drop_table(conn, table_name):
    """ create a table from the table_name statement
    :param conn: Connection object
    :param table_name: name of the table to create
    :return:
    """
    try:
        c = conn.cursor()
        sql_drop_table = f"""DROP TABLE Table_{table_name}"""
        c.execute(sql_drop_table)
    except Error as e:
        print(e)
def main():
    database = "my_dbfile.db"
    country_with_code = {
        "USA": "United_States_of_America",
        "IND": "India",
        "PHIL": "Philipines",
        "BOS" : "Bosnia",
        "AU" : "Australia"
    }
    conn = create_connection(database)
    for code in country_with_code:
        table_name = scrub(country_with_code[code])
        drop_table(conn, table_name)
if __name__ == '__main__':
    main()


