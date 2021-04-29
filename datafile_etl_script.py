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
def create_table(conn, table_name):
    """ create a table from the table_name statement
    :param conn: Connection object
    :param table_name: name of the table to create
    :return:
    """
    try:
        c = conn.cursor()
        sql_create_table = f"""CREATE TABLE IF NOT EXISTS Table_{table_name} (
                                    Customer_Name text PRIMARY KEY,
                                    Customer_ID text NOT NULL,
                                    Customer_Open_Date text NOT NULL,
                                    Last_Consulted_Date text,
                                    Vaccination_Type text,
                                    Doctor_Consulted text,
                                    State text,
                                    Country text,
                                    Date_of_Birth text,
                                    Active_Customer text
                                );"""
        c.execute(sql_create_table)
    except Error as e:
        print(e)
def insert_table(conn, table_name, to_db):
    """ create a table from the table_name statement
    :param conn: Connection object
    :param table_name: name of the table to create
    :return:
    """
    try:
        c = conn.cursor()
        sql_insert_table = f"""INSERT INTO Table_{table_name}
        (Customer_Name, Customer_ID, Customer_Open_Date, Last_Consulted_Date, Vaccination_Type, Doctor_Consulted, State, Country, Date_of_Birth, Active_Customer) VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        c.execute(sql_insert_table, to_db)
        conn.commit()
    except Error as e:
        print(e)
def scrub(table_name):
    """ create a table names only in alphanumerics
    scrubing off characters that may be misued for sql injection
    :param table_name: name of the table to create
    :return: name with only alphanumeric characters
    """
    return ''.join( chr for chr in table_name if chr.isalnum() )

def main():
    database = "my_dbfile.db"
    datafile = "datafile.csv"
    conn = create_connection(database)
    country_with_code = {
        "USA": "United_States_of_America",
        "IND": "India",
        "PHIL": "Philipines",
        "BOS" : "Bosnia",
        "AU" : "Australia"
    }
    for code in country_with_code:
        table_name = scrub(country_with_code[code])
        create_table(conn, table_name)
    with open(datafile, 'r') as file:
        reader = list(csv.reader(file,  delimiter='|'))[1:]
        row_counter = 0
        for row in reader:
            row_counter += 1
            try:
                table_name = scrub(country_with_code[row[9]])
            except KeyError:
                print(f"Country code not available for {row[9]}")
                continue
            insert_table(conn, table_name, row[2:12])
    print(f"Processed {row_counter} data rows of {datafile} file")
if __name__ == '__main__':
    main()
