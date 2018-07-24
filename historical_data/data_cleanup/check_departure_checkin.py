from data_cleanup.check_booked import validate_date


def update_departure_checkin(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["departure"]
    for row in read_file:
        departure_in_file = row[header_to_look_for]
        formatted_departure = validate_date(departure_in_file)
        row["departure"] = formatted_departure
    return read_file
