import sqlite3
from sqlite3 import Error

def sql_connection():
    """ Create a connection with SQLite database specified
        by the books.db file
    :param con: the connection object
    :return: connection object or Error"""
    try:
        db = sqlite3.connect('books.db')
        return db
    except Error as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": str(e)}

def create_books_table():
    """ Create the table with given columns
    """
    try:
        con = sql_connection()
        cur = con.cursor()
        cur.execute('''DROP TABLE IF EXISTS books''')
        cur.execute(
        '''CREATE TABLE books(
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        year TEXT,
        logo TEXT,
        description TEXT);'''
                    )
        con.commit()
        print('The table is created successfully')
    except Error as e:
        print(e)

create_books_table()