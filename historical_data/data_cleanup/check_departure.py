
def update_departure(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["employee_id"]
    for row in read_file:
        employee_id_in_file = row[header_to_look_for]
        row["employee_id"] = employee_id_in_file
    return read_file
