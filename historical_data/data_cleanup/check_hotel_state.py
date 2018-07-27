from data_cleanup.python_mysql_connect import connect_to_database


def update_hotel_state(read_file, headers_in_file):

    header_to_look_for = headers_in_file["hotel_state_id"]

    for row in read_file:
        if row.get(header_to_look_for) is not None:
            hotel_state_in_file = row[header_to_look_for]
            if hotel_state_in_file != "":
                hotel_country_in_file = str(row["hotel_country_id"])
                hotel_state = _validate_hotel_state(hotel_state_in_file, hotel_country_in_file)
                row["hotel_state_id"] = hotel_state[0]
            else:
                row["hotel_state_id"] = ""
    return read_file


def _validate_hotel_state(state_in_file, country_in_file):

    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        search_results = _search_by_subdivision_alias(cursor, state_in_file, country_in_file)
        if search_results is None:
            search_results = _search_by_iso_2_code_with_country(cursor, state_in_file, country_in_file)
            if search_results is None:
                search_results = _search_by_iso_2_code_without_country(cursor, state_in_file, country_in_file)
                if search_results is None:
                    search_results = _search_similar_subdivisions(cursor, state_in_file, country_in_file)
                    if search_results is None:
                        search_results = _missing_state(cursor, state_in_file, country_in_file)
                        _update_database_with_new_subdivision_alias(historical_db_connection, cursor, state_in_file, search_results)
        return search_results
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def _search_by_subdivision_alias(cursor, state_to_search_for, country_id_to_search_for):

    query = "SELECT subdivisions_aliases.subdivision_id " \
            "FROM subdivisions_aliases " \
            "JOIN subdivisions " \
            "ON subdivisions_aliases.subdivision_id = subdivisions.id " \
            "WHERE subdivisions_aliases.alias_name =  %s " \
            "AND subdivisions.country_id = %s"
    data = (state_to_search_for, country_id_to_search_for)
    cursor.execute(query, data)
    results = cursor.fetchone()
    return results


def _search_by_iso_2_code_with_country(cursor, state_to_search_for, country_id_to_search_for):

    query = "SELECT id " \
            "FROM subdivisions " \
            "WHERE iso_3166_2_code =  %s " \
            "AND country_id = %s"
    data = (state_to_search_for, country_id_to_search_for)
    cursor.execute(query, data)
    results = cursor.fetchone()
    return results


def _search_by_iso_2_code_without_country(cursor, state_to_search_for, country_id_to_search_for):

    query = "SELECT id " \
            "FROM subdivisions " \
            "WHERE SUBSTRING(iso_3166_2_code FROM 4) =  %s " \
            "AND country_id = %s"
    data = (state_to_search_for, country_id_to_search_for)
    cursor.execute(query, data)
    results = cursor.fetchone()
    return results


def _search_similar_subdivisions(cursor, state_to_search_for, country_id_to_search_for):

    query = "SELECT id " \
            "FROM subdivisions " \
            "WHERE iso_3166_2_code LIKE %s " \
            "AND country_id = %s"
    updated_like_string = "%"+state_to_search_for+"%"
    data = (updated_like_string, country_id_to_search_for)
    cursor.execute(query, data)
    results = cursor.fetchone()
    return results


def _missing_state(cursor, missing_state, missing_country):

    country = _find_country_name(cursor, missing_country)
    country_name = country[0]
    print(missing_state + " is not an identified state of " + country_name)
    print("The following states are available in " + country_name + ":")
    state_options = _suggest_similar_states(cursor, missing_country)
    _print_suggestions(state_options)
    selected_state = input("What state should it be mapped to? (please enter the ID) ")
    return selected_state


def _find_country_name(cursor, country_id):
    query = "SELECT country_formal_name " \
            "FROM countries " \
            "WHERE id =  %s"
    cursor.execute(query, country_id)
    country_name = cursor.fetchone()
    return country_name


def _suggest_similar_states(cursor, missing_country):

    query = "SELECT subdivision_name, " \
            "iso_3166_2_code, " \
            "id " \
            "FROM subdivisions " \
            "WHERE country_id = %s"
    cursor.execute(query, missing_country)
    result = cursor.fetchall()
    return result


def _print_suggestions(suggested_states):
    for suggestion in suggested_states:
        print(suggestion)


def _update_database_with_new_subdivision_alias(connection, cursor, missing_alias, missing_subdivision_id):

    update_query = "INSERT INTO subdivisions_aliases (alias_name, subdivision_id) " \
                   "VALUES (%s, %s)"
    data = (missing_alias, missing_subdivision_id)
    print(data)
    cursor.execute(update_query, data)
    connection.commit()
