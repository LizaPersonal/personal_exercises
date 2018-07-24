from data_cleanup.python_mysql_connect import connect_to_database


def update_hotel_state(read_file, headers_in_file):

    header_to_look_for = headers_in_file["hotel_state_id"]

    for row in read_file:
        if row.get(header_to_look_for) is not None:
            hotel_state_in_file = row[header_to_look_for]
            if hotel_state_in_file != "":
                hotel_country_in_file = str(row["hotel_country_id"])
                hotel_state = _hotel_state_from_db(hotel_state_in_file, hotel_country_in_file)
                row["hotel_state_id"] = hotel_state[0]
            else:
                row["hotel_state_id"] = ""
    return read_file


def _hotel_state_from_db(state_in_file, country_in_file):

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


# def _confirm_country(cursor, state_id_to_search_for, country_id_to_search_for):
#
#     query = "SELECT country_id " \
#             "FROM subdivisions " \
#             "WHERE id =  %s"
#     cursor.execute(query, state_id_to_search_for)
#     country_id_result = cursor.fetchone()
#     if country_id_result[0] == country_id_to_search_for:
#         return True
#     else:
#         return False
