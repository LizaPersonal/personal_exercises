
def updated_route(read_file, flight_headers_in_file, destination_symbol, connecting_symbol, openjaw_symbol):
    """ Identify which column represents the route.
        Update the file with the route to match Rocketrip standards. """

    header_to_look_for = flight_headers_in_file["route"]
    for row in read_file:
        route_in_file = row[header_to_look_for]
        route = _validate_route_icons(route_in_file, destination_symbol, connecting_symbol, openjaw_symbol)
        row["route"] = route
    return read_file


def _validate_route_icons(route_in_file, destination_icon, connecting_icon, openjaw_icon):
    """ Take in a route and what the indicators are for this file.
        Clean the route to match the expected value in our database. """

    updated_openjaw_route = _clean_route(route_in_file, openjaw_icon, "*")
    updated_connecting_route = _clean_route(updated_openjaw_route, connecting_icon, "-")
    final_route = _clean_route(updated_connecting_route, destination_icon, "/")
    return final_route


# def _define_order_of_cleanup(destination_icon, connecting_icon, openjaw_icon):
#     final_icons = ["/", "-", "*"]
#     order = {}
#     if destination_icon in final_icons:
#         order['first'] = destination_icon
#     elif connecting_icon in final_icons:
#         order['first'] = connecting_icon
#     elif openjaw_icon in final_icons:
#         order['first'] = openjaw_icon
#     return order


def _clean_route(route_in_file, icon_in_file, correct_icon):
    """ Take the route and find if the icon is in the route.
        If so, update the route with the correct icon. """

    new_route = route_in_file
    if icon_in_file != correct_icon:
        if icon_in_file in route_in_file:
            new_route = route_in_file.replace(icon_in_file, correct_icon)
    return new_route
