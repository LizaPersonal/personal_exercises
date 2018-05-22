from data_cleanup.python_mysql_connect import connect_to_database


def updated_route_destinations(read_file, flight_headers_in_file):
    """ Identify which column represents the route and the domestic/international.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_to_look_for = flight_headers_in_file["route"]
    header_to_update = flight_headers_in_file["route_destinations"]
    if header_to_update == "":
        header_to_update = "route_destinations"
    for row in read_file:
        route = row[header_to_look_for]
        route_destinations = _route_destinations(route)
        row[header_to_update] = route_destinations
    return read_file


def _route_destinations(route_in_file):
    """ Connect to the historical database.
        Search in the airports table for the airports in the route from the file.
        Close the connection to historical database. """

    cursor = None
    historical_db_connection = None
    try:
        historical_db_connection = connect_to_database()
        cursor = historical_db_connection.cursor()
        airports = identify_airports_in_route(route_in_file)
        destinations = ""
        for airport in airports:
            destinations += airport + "/"
        destinations = destinations[:-1]
        return destinations
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if historical_db_connection:
            historical_db_connection.close()


def identify_airports_in_route(route):
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
