from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def connect_to_database():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn: object = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    return conn


# def connect_to_historical_database():
#
#     db_config = """host='customerhistorical-vpc-enc.cvhe9o57xgm1.us-east-1.rds.amazonaws.com',
#                    user='readwrite',
#                    password='analyzerforwriter1234',
#                    database='historical'"""
#
#     try:
#         print('Connecting to MySQL database...')
#         connection = mysql.connector.connect(db_config)
#
#         if connection.is_connected():
#             print('connection established.')
#         else:
#             print('connection failed.')
#
#     except e:
#         print(e)
#
#     return connection


# connect = connect_to_database()
# connect.close()
