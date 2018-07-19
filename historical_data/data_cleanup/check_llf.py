from data_cleanup.check_base_price import check_price_format


def update_llf(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["llf"]
    for row in read_file:
        llf_in_file = row[header_to_look_for]
        llf = check_price_format(llf_in_file)
        row["llf"] = llf
    return read_file
