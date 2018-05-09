from data_cleanup.python_mysql_connect import connect_to_database


class GeneralError(Exception):
    pass


class NotValidAirline(Exception):
    pass


def validate_airline_vendor(airline_in_file):
    """ Connect to the historical database.
        Search in the airlines table for the airline from the file.
        If the airline does not exist, update the table based on user input.
        Close the connection to historical database. """
    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        search_results = _search_airline_database(cursor, airline_in_file)
        if search_results is None:
            missing_airline = airline_in_file[0]
            update_vendor_code = _get_new_airline_code(missing_airline)
            _update_database_with_new_airline(historical_db_connection, cursor, missing_airline, update_vendor_code)
            search_results = (update_vendor_code, missing_airline)
        else:
            print(airline_in_file[0] + ' ---> ' + str(search_results))
        return search_results
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def _search_airline_database(cursor, airline_to_search_for):
    """ Search for the airline from the file in the historical database table airlines. """
    query = "SELECT airline_code FROM airlines WHERE airline_fullname = %s"
    cursor.execute(query, airline_to_search_for)
    results = cursor.fetchone()
    return results


def _get_new_airline_code(missing_airline):
    """ If the airline from the file doesn't exist in the database yet,
        request what the airline code should be from the user. """
    update_vendor_code = input(missing_airline + """ vendor does not exist yet, what should it be mapped to?
        You can look it up here: http://www.iata.org/publications/Pages/code-search.aspx\n""")
    return update_vendor_code


def _update_database_with_new_airline(connection, cursor, missing_airline, missing_vendor_code):
    """ Update the historical database table airlines,
        with the missing airline and airline code provided by the user. """
    update_query = "INSERT INTO airlines (airline_fullname, airline_code) VALUES (%s, %s)"
    data = (missing_airline, missing_vendor_code)
    print(data)
    cursor.execute(update_query, data)
    connection.commit()
