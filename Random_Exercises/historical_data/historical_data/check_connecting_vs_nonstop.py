
def nonstop_or_connecting(route_in_file):
    if "-" in route_in_file:
        return "Connecting"
    else:
        return "Nonstop"
