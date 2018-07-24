from data_cleanup.check_booked import validate_date


def update_checkout(read_file, headers_in_file):

    header_to_look_for = headers_in_file["checkout"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            checkout_in_file = row[header_to_look_for]
            formatted_checkout = validate_date(checkout_in_file)
            row["checkout"] = formatted_checkout
    return read_file