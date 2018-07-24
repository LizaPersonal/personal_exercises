from data_cleanup.python_mysql_connect import connect_to_database


def update_hotel_country(read_file, headers_in_file):

    header_to_look_for = headers_in_file["hotel_country_id"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            hotel_country_in_file = row[header_to_look_for]
            hotel_country = _hotel_country_from_db(hotel_country_in_file)
            row["hotel_country_id"] = hotel_country[0]
    return read_file


def _hotel_country_from_db(country_in_file):

    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        search_results = _search_by_counrty_alias(cursor, country_in_file)
        if search_results is None:
            search_results = _search_by_iso_2_code(cursor, country_in_file)
            if search_results is None:
                search_results = _search_by_iso_3_code(cursor, country_in_file)
        return search_results
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def _search_by_counrty_alias(cursor, country_to_search_for):

    query = "SELECT country_id FROM countries_aliases WHERE alias_name =  %s"
    cursor.execute(query, country_to_search_for)
    results = cursor.fetchone()
    return results


def _search_by_iso_2_code(cursor, country_to_search_for):

    query = "SELECT id FROM countries WHERE iso_alpha_2_code =  %s"
    cursor.execute(query, country_to_search_for)
    results = cursor.fetchone()
    return results


def _search_by_iso_3_code(cursor, country_to_search_for):

    query = "SELECT id FROM countries WHERE iso_alpha_3_code =  %s"
    cursor.execute(query, country_to_search_for)
    results = cursor.fetchone()
    return results
