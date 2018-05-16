
def nonstop_or_connecting(route_in_file):
    """ Take in a route and identify if there is an indication for connecting. """

    if "-" in route_in_file:
        return "Connecting"
    else:
        return "Nonstop"
