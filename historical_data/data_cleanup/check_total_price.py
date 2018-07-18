from data_cleanup.check_base_price import check_price_format


def update_total_price(read_file, flight_headers_in_file):

    header_for_total_price = flight_headers_in_file["total_price"]
    header_for_base_price = flight_headers_in_file["base_price"]
    header_for_taxes_and_fees = flight_headers_in_file["taxes_and_fees"]

    for row in read_file:
        total_price_in_file = row[header_for_total_price]
        base_price_in_file = row[header_for_base_price]
        taxes_and_fees_in_file = row[header_for_taxes_and_fees]
        if total_price_in_file != "":
            total_price = check_price_format(total_price_in_file)
        else:
            total_price = float(base_price_in_file) + float(taxes_and_fees_in_file)
        row["total_price"] = total_price
    return read_file
