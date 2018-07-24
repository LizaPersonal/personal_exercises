from data_cleanup.check_booked import validate_date


def update_departure(read_file, headers_in_file):

    header_to_look_for = headers_in_file["departure"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            departure_in_file = row[header_to_look_for]
            formatted_departure = validate_date(departure_in_file)
            row["departure"] = formatted_departure
    return read_file
