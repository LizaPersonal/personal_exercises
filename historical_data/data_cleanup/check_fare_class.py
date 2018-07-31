from data_cleanup.python_mysql_connect import connect_to_database


def update_fare_class(read_file, headers_in_file):
    """ Identify which column represents the fare class.
        For each row search in the database in the fare class table for the expected standardized fare class.
        Update the file with the expected standardized fare class. """

    header_to_look_for = headers_in_file["fare_class"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            fare_class_in_file = row[header_to_look_for]
            expected_fare_class = _validate_fare_class((fare_class_in_file, ))
            row["fare_class"] = expected_fare_class[0]
    return read_file


def _validate_fare_class(fare_class_in_file):
    """ Connect to the historical database.
        Search in the fare_class table for the fare class from the file.
        If the fare class does not exist, update the table based on user input.
        Close the connection to historical database. """

    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        search_results = _search_fare_class_database(cursor, fare_class_in_file)
        if search_results is None:
            missing_fare_class = fare_class_in_file[0]
            updated_fare_class = _get_new_fare_class(missing_fare_class)
            _update_database_with_new_fare_class(historical_db_connection, cursor, missing_fare_class, updated_fare_class)
            search_results = (updated_fare_class, missing_fare_class)
        return search_results
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def _search_fare_class_database(cursor, fare_class_to_search_for):
    """ Search for the fare class from the file in the historical database table fare_classes. """

    query = "SELECT standardized_value " \
            "FROM fare_classes " \
            "WHERE tmc_value = %s"
    cursor.execute(query, fare_class_to_search_for)
    results = cursor.fetchone()
    return results


def _get_new_fare_class(missing_fare_class):
    """ If the fare class from the file doesn't exist in the database yet,
        request what the fare class standardization should be from the user. """

    updated_fare_class = ""
    while updated_fare_class not in ["Economy", "Premium Economy", "Business", "First", "Unknown"]:
        print(missing_fare_class + " fare class does not exist yet, what should it be mapped to?")
        print("Economy, Premium Economy, Business, First, or Unknown")
        updated_fare_class = input()
    return updated_fare_class


def _update_database_with_new_fare_class(connection, cursor, missing_fare_class, missing_standardized_fare_class):
    """ Update the historical database table fare_classes,
        with the missing fare class and the standardized fare class provided by the user. """

    update_query = "INSERT INTO fare_classes (tmc_value, standardized_value) VALUES (%s, %s)"
    data = (missing_fare_class, missing_standardized_fare_class)
    print(data)
    cursor.execute(update_query, data)
    connection.commit()
