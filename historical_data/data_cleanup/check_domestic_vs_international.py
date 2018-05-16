from data_cleanup.python_mysql_connect import connect_to_database


def updated_domestic_vs_international(read_file, flight_headers_in_file):
    """ Identify which column represents the route and the domestic/international.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_to_look_for = flight_headers_in_file["route"]
    header_to_update = flight_headers_in_file["dom_or_int"]
    for row in read_file:
        route = row[header_to_look_for]
        domestic_international = _domestic_or_international(route)
        row[header_to_update] = domestic_international
    return read_file


def _domestic_or_international(route_in_file):
    """ Connect to the historical database.
        Search in the airports table for the airports in the route from the file.
        Close the connection to historical database. """

    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        airports = _identify_airports_in_route(route_in_file)
        countries = []
        for airport in airports:
            countries.append(_search_airport_for_country(cursor, airport))
        if _compare_countries(countries) is True:
            return "Domestic"
        else:
            return "International"
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def _identify_airports_in_route(route):
    """ Take in a route and identify each airport. """

    airports = []
    character_count = 0
    while character_count < len(route):
        airport_name = route.find("/", character_count)
        if airport_name == -1:
            airports.append(route[character_count:(character_count + 3)])
            return airports
        else:
            airports.append(route[character_count:(character_count+3)])
            character_count = airport_name + 1
    return airports


def _search_airport_for_country(cursor, airport_to_search_for):
    """ Search for the airport country from the file in the historical database table airport. """

    query = "SELECT country FROM airports WHERE iata = %s"
    cursor.execute(query, airport_to_search_for)
    results = cursor.fetchone()
    return results


def _compare_countries(countries):
    """ Look at all countries in a list and confirm if they are the same or not. """

    start_country = countries[0]
    for country in countries:
        if country == start_country:
            return True
        else:
            return False
