# Helper functions for app.py

from datetime import datetime
import mysql.connector
from mysql.connector import errorcode

def connect(config):
    """Returns a connection to a database.

    Keyword arguments:
    config -- the configuration of credentials to access the database, including,
              but not limited to, username, password, host, and database name
    """
    try:
        print("Connecting to database...")
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        print("Successfully connected to database.")
        return conn, cursor    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
        return
    

def create_database(cursor, DB_NAME):
    """Creates a database.

    Keyword arguments:
    cursor -- the cursor to a given database
    DB_NAME -- name of the database to create
    """
    try:
        cursor.execute(
            "Creating database: {}".format(DB_NAME)
        )
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def get_datetime():
    """Returns the current date and time in as a string."""

    return str(datetime.now())