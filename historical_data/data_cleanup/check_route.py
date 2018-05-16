
def validate_route_icons(route_in_file, destination_icon, connecting_icon, openjaw_icon):
    """ Take in a route and what the indicators are for this file.
        Clean the route to match the expected value in our database. """

    updated_destination_route = _clean_route(route_in_file, destination_icon, "/")
    updated_connecting_route = _clean_route(updated_destination_route, connecting_icon, "-")
    final_route = _clean_route(updated_connecting_route, openjaw_icon, "*")
    return final_route


def _clean_route(route_in_file, icon_in_file, correct_icon):
    """ Take the route and find if the icon is in the route.
        If so, update the route with the correct icon. """

    if icon_in_file != correct_icon:
        if icon_in_file in route_in_file:
            route_in_file.replace(icon_in_file, correct_icon)
    return route_in_file
