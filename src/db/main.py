import os

import sqlite3


PATH = os.getenv('DB_PATH')


def connect():
    """
    Create a connection to the PostgreSQL Control-database by psycopg2
    :return:
    """
    return sqlite3.connect(PATH, check_same_thread=False)
