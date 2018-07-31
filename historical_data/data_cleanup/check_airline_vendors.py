from data_cleanup.check_employee_name import set_name_to_correct_case
from data_cleanup.python_mysql_connect import connect_to_database


def update_airline_vendor(read_file, headers_in_file):
    """ Identify which column represents the vendor.
        For each row search in the database in the airlines table for the vendor code.
        Update the file with the vendor code rather than vendor name. """

    header_to_look_for = headers_in_file["vendor"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            airline_in_file = row[header_to_look_for]
            vendor_code = _validate_airline_vendor((airline_in_file,))
            row["vendor"] = vendor_code[0]
    return read_file


def _validate_airline_vendor(airline_in_file):
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
            missing_airline = set_name_to_correct_case(missing_airline)
            update_vendor_code = _get_new_airline_code(cursor, missing_airline)
            if _check_suggested_vendor_code(cursor, update_vendor_code):
                _update_database_with_new_airline_alias(historical_db_connection, cursor, missing_airline, update_vendor_code)
            else:
                iata_numeric, airline_icao, airline_country, airline_active, airline_low_cost = \
                    _collect_additional_new_airline_info(missing_airline, update_vendor_code)
                _update_database_with_new_airline(historical_db_connection, cursor, missing_airline, update_vendor_code,
                                                  iata_numeric, airline_icao, airline_country, airline_active, airline_low_cost)
                _update_database_with_new_airline_alias(historical_db_connection, cursor, missing_airline,
                                                        update_vendor_code)
            search_results = (update_vendor_code, missing_airline)
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

    query = "SELECT iata_alpha_2_code " \
            "FROM airlines " \
            "JOIN airlines_aliases " \
            "ON airlines.id = airlines_aliases.airline_id " \
            "WHERE airlines_aliases.airline_alias_name = %s"
    cursor.execute(query, airline_to_search_for)
    results = cursor.fetchone()
    return results


def _get_new_airline_code(cursor, missing_airline):
    """ If the airline from the file doesn't exist in the database yet,
        request what the airline code should be from the user. """

    print(missing_airline + """ vendor does not exist yet, what should it be mapped to?\n 
Here are some other similar options already in the database:""")
    print(_suggest_similar_airlines(cursor, missing_airline))
    print("""\nOr you can look up the airline here: 
http://www.iata.org/publications/Pages/code-search.aspx\n""")
    update_vendor_code = input("Please, only enter the 2 digit code:\n")
    return update_vendor_code


def _suggest_similar_airlines(cursor, missing_airline):

    results = []
    query = "SELECT airlines_aliases.airline_alias_name, " \
            "airlines.iata_alpha_2_code " \
            "FROM airlines " \
            "JOIN airlines_aliases " \
            "ON airlines.id = airlines_aliases.airline_id " \
            "WHERE airlines_aliases.airline_alias_name LIKE %s"
    words = missing_airline.split()
    for word in words:
        data = '%'+word+'%'
        cursor.execute(query, data)
        result = cursor.fetchmany()
        if result != ():
            results.append(result[0])
    return results


def _check_suggested_vendor_code(cursor, suggested_vendor_code):

    query = "SELECT iata_alpha_2_code " \
            "FROM airlines " \
            "WHERE airlines.iata_alpha_2_code = %s"
    cursor.execute(query, suggested_vendor_code)
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True


def _update_database_with_new_airline_alias(connection, cursor, missing_airline, missing_vendor_code):

    update_query = "INSERT INTO airlines_aliases (airlines_aliases.airline_alias_name, airlines_aliases.airline_id) " \
                   "VALUES (%s, (SELECT airlines.id " \
                   "FROM airlines " \
                   "WHERE airlines.iata_alpha_2_code = %s))"
    data = (missing_airline, missing_vendor_code)
    print(data)
    cursor.execute(update_query, data)
    connection.commit()


def _collect_additional_new_airline_info(missing_airline, missing_vendor_code):

    print(missing_vendor_code + " is a new iata code not currently in the database. "
                                "Please provide some additional information for this new airline " + missing_airline)
    iata_numeric = _convert_input_empty_string_to_null(input("What is the IATA numberic code?\n"))
    icao_code = _convert_input_empty_string_to_null(input("What is the ICAO code?\n"))
    country = _convert_input_empty_string_to_null(input("Where are the airline headquarters? (Country)\n"))
    active_acceptable_value = 2
    while active_acceptable_value == 2:
        active = input("Is this airline still in service? (Y/N)\n")
        active_acceptable_value = _convert_input_to_binary(active)
    low_cost_acceptable_value = 2
    while low_cost_acceptable_value == 2:
        low_cost_carrier = input("Is this a low cost carrier? (Y/N)\n")
        low_cost_acceptable_value = _convert_input_to_binary(low_cost_carrier)
    return iata_numeric, icao_code, country, active_acceptable_value, low_cost_acceptable_value


def _convert_input_to_binary(input):
    if input == 'Y':
        return 1
    elif input == 'N':
        return 0
    else:
        return 2


def _convert_input_empty_string_to_null(input):
    if input == '':
        return 'NULL'
    else:
        return input


def _update_database_with_new_airline(connection, cursor, new_airline, iata_alpha, iata_numeric, icao, country, active, low_cost):

    update_query = "INSERT INTO airlines (airline_formal_name, iata_alpha_2_code, iata_numeric_code, " \
                   "icao_alpha_3_code, country_id, is_active, low_cost_carrier) " \
                   "VALUES (%s, %s, %s, %s, (SELECT country_id " \
                   "FROM countries_aliases " \
                   "WHERE countries_aliases.alias_name = %s), %s, %s)"
    data = (new_airline, iata_alpha, iata_numeric, icao, country, active, low_cost)
    print(data)
    cursor.execute(update_query, data)
    connection.commit()
