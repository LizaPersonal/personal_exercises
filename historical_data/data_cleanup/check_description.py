
def update_description(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["description"]
    for row in read_file:
        description_in_file = row[header_to_look_for]
        row["description"] = description_in_file
    return read_file
