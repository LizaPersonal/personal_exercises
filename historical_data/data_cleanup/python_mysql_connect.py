import pymysql
from data_cleanup.python_mysql_dbconfig import read_db_config


def connect_to_database():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = pymysql.connect(**db_config)

    except Exception as error:
        print(error)

    return conn

