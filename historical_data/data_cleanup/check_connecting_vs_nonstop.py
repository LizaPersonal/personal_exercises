
def update_connecting_vs_nonstop(read_file):
    """ Identify which column represents the route and the nonstop/connecting.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_to_look_for = "route"
    for row in read_file:
        route = row[header_to_look_for]
        nonstop_connecting = _nonstop_or_connecting(route)
        row["nonstop_or_connecting"] = nonstop_connecting
    return read_file


def _nonstop_or_connecting(route_in_file):
    """ Take in a route and identify if there is an indication for connecting. """

    if "-" in route_in_file:
        return "Connecting"
    else:
        return "Nonstop"
