from data_cleanup.check_base_price import check_price_format


def update_taxes_and_fees(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["taxes_and_fees"]
    for row in read_file:
        base_price_in_file = row[header_to_look_for]
        base_price = check_price_format(base_price_in_file)
        row["taxes_and_fees"] = base_price
    return read_file
