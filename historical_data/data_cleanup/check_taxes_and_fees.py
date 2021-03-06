from data_cleanup.check_base_price import check_price_format


def update_taxes_and_fees(read_file, headers_in_file):

    header_to_look_for = headers_in_file["taxes_and_fees"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            taxes_and_fees_in_file = row[header_to_look_for]
            if taxes_and_fees_in_file != "":
                taxes_and_fees = check_price_format(taxes_and_fees_in_file)
                row["taxes_and_fees"] = taxes_and_fees
            else:
                row["taxes_and_fees"] = taxes_and_fees_in_file
    return read_file
