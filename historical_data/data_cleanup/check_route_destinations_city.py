from data_cleanup.check_route_destinations import identify_airports_in_route
from data_cleanup.python_mysql_connect import connect_to_database


def updated_route_destinations_city(read_file):
    """ Identify which column represents the route and the domestic/international.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_to_look_for = "route"
    for row in read_file:
        route = row[header_to_look_for]
        route_destinations_city = _route_destinations_city(route)
        row["route_destinations_city"] = route_destinations_city
    return read_file


def _route_destinations_city(route_in_file):
    """ Connect to the historical database.
        Search in the airports table for the airports in the route from the file.
        Close the connection to historical database. """

    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        airports = identify_airports_in_route(route_in_file)
        destination_city = ""
        for airport in airports:
            destination_city += _search_airport_for_destination_country(cursor, airport)[0] + "/"
        destination_city = destination_city[:-1]
        return destination_city
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def _search_airport_for_destination_country(cursor, airport_to_search_for):
    """ Search for the airport country from the file in the historical database table airport. """

    query = "SELECT airport_city FROM airports WHERE iata = %s"
    cursor.execute(query, airport_to_search_for)
    results = cursor.fetchone()
    return results
