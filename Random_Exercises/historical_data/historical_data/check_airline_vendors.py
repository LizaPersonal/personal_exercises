import mysql.connector
from python_mysql_connect import connect_to_database


def validate_airline_vendor(airline_in_file):
    historical_db_connection = connect_to_database()
    cursor = historical_db_connection.cursor()
    search_results = _search_airline_database(cursor, airline_in_file)

    try:
        if search_results is None:
            missing_airline = airline_in_file[0]
            update_vendor_code = _get_new_airline_code(missing_airline)
            _update_database_with_new_airline(historical_db_connection, cursor, missing_airline, update_vendor_code)
            search_results = update_vendor_code
        else:
            print(airline_in_file[0] + ' ---> ' + str(search_results))
        cursor.close()
        historical_db_connection.close()
        return search_results
    except e:
        print(e)


def _search_airline_database(cursor, airline_to_search_for):
    query = "SELECT airline_code FROM airlines WHERE airline_fullname = %s"
    cursor.execute(query, airline_to_search_for)
    results = cursor.fetchone()
    return results


def _get_new_airline_code(missing_airline):
    update_vendor_code = input(missing_airline + """ vendor does not exist yet, what should it be mapped to?
        You can look it up here: http://www.iata.org/publications/Pages/code-search.aspx\n""")
    return update_vendor_code


def _update_database_with_new_airline(connection, cursor, missing_airline, missing_vendor_code):
    update_query = "INSERT INTO airlines (airline_fullname, airline_code) VALUES ('SwissAir', 'LX')"
    data = (missing_airline, missing_vendor_code)
    print(data)
    cursor.execute(update_query)
    connection.commit()


#
# open_connection = connect_to_historical_database()
# validate_airline_vendor(open_connection, )


