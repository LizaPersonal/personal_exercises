from data_cleanup.check_base_price import check_price_format


def update_llf(read_file, headers_in_file):

    header_to_look_for = headers_in_file["llf"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            llf_in_file = row[header_to_look_for]
            llf = check_price_format(llf_in_file)
            row["llf"] = llf
    return read_file
