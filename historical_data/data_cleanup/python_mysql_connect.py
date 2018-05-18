import pymysql
from data_cleanup.python_mysql_dbconfig import read_db_config


def connect_to_database():
    """ Connect to MySQL database """

    db_config = read_db_config()
    try:
        conn = pymysql.connect(**db_config)
    except Exception as error:
        print(error)
    return conn


# def data_standardization_from_database_table(value_to_standardize_from_file):
#     """ Connect to the historical database.
#         Search in the fare_class table for the fare class from the file.
#         If the fare class does not exist, update the table based on user input.
#         Close the connection to historical database. """
#
#     cursor = None
#     historical_db_connection = None
#     try:
#         historical_db_connection = connect_to_database()
#         cursor = historical_db_connection.cursor()
#         search_results = _search_table_in_database(cursor, value_to_standardize_from_file)
#         if search_results is None:
#             missing_value_in_table = value_to_standardize_from_file[0]
#             update_value_to_table = _get_new_value_for_database(missing_value_in_table)
#             _update_database_with_new_airline(historical_db_connection, cursor, missing_airline, update_vendor_code)
#             search_results = (update_value_to_table, missing_value_in_table)
#         else:
#             print(fare_class_in_file[0] + ' ---> ' + str(search_results))
#         return search_results
#     except Exception as e:
#         print(e)
#     finally:
#         if cursor:
#             cursor.close()
#         if historical_db_connection:
#             historical_db_connection.close()
#
#
# def _get_new_value_for_database(missing_value, type_searching_for_in_database):
#     """ If the airline from the file doesn't exist in the database yet,
#         request what the airline code should be from the user. """
#
#     update_mapping_value = input(missing_value + " does not exist yet as a " + type_searching_for_in_database
#                                + ". What should it be mapped to?")
#     return update_mapping_value
