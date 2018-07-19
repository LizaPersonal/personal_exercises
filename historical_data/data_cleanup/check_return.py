from data_cleanup.check_booked import validate_date


def update_return(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["return"]
    for row in read_file:
        return_in_file = row[header_to_look_for]
        formatted_return = validate_date(return_in_file)
        row["return"] = formatted_return
    return read_file
