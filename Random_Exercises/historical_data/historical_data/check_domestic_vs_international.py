
def domestic_or_international(route_in_file):
    if "-" in route_in_file:
        return "Connecting"
    else:
        return "Nonstop"