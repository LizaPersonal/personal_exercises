def update_total_price(read_file, flight_headers_in_file):
    """ Identify which column represents the route and the nonstop/connecting.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_for_total_price = flight_headers_in_file["total_price"]
    header_for_base_price = flight_headers_in_file["base_price"]
    header_for_taxes_and_fees = flight_headers_in_file["taxes_and_fees"]

    for row in read_file:
        route = row[header_to_look_for]
        nonstop_connecting = _nonstop_or_connecting(route)
        row[header_to_update] = nonstop_connecting
    return read_file


def _calculate_total_price(base_price_in_file, taxes_and_fees_in_file, total_price_in_file):
    """ Take in a base price and tax, and calculate the total price. """

    if total_price_in_file == "" and base_price_in_file != "":
        total_price = base_price_in_file + taxes_and_fees_in_file
    elif total_price_in_file != "" and base_price_in_file != "":
        if total_price_in_file == (base_price_in_file + taxes_and_fees_in_file):
            total_price = total_price_in_file
        
        return "Nonstop"
    return total_price

def _check_