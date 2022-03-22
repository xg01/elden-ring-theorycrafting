import sqlite3 
from sqlite3 import Error

def create_connection(db_file):
    """ Creates a connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite Version: {sqlite3.version}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    """ Creates a table from the create_table_sql statement """ 
    try: 
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_character(conn, char):
    """ Creates a new project into the projects table """
    sql = ''' INSERT INTO characters(name, stats)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit() 

    return cur.lastrowid

