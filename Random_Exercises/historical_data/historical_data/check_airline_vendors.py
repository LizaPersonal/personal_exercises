from mysql.connector import MySQLConnection, Error
from .python_mysql_connect import connect


def check_column(connection, column_header_to_check,):
    airline_vendors = connection.cursor.fetchall()

    for vendor in airline_vendors:
        if file_vendor_column == vendor:
            print("Item exists")
        else:
            print("This vendor does not exist yet, what should it be mapped to?")


