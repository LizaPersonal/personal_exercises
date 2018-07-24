from data_cleanup.check_booked import validate_date


def update_checkin(read_file, headers_in_file):

    header_to_look_for = headers_in_file["checkin"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            checkin_in_file = row[header_to_look_for]
            formatted_checkin = validate_date(checkin_in_file)
            row["checkin"] = formatted_checkin
    return read_file