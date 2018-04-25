from mysql.connector import MySQLConnection, Error
from .python_mysql_connect import connect


def update_flight_table(conn, data):

    query = """ UPDATE flight
                SET employee_name = %s,
                    employee_id = %s,
                    organization = %s,
                    fare_class = %s
            """
    try:
        cursor = conn.cursor()
        cursor.execute(query, data)

        conn.commit()

    except Error as error:

        print(error)

    finally:

        cursor.close()


def update_hotel_table():
    pass


def update_car_table():
    pass


def update_rail_table():
    pass


if __name__ == '__main__':
    connect_to_historical_read_write = connect()

    connect_to_historical_read_write.close()
