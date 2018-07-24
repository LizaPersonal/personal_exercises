
def update_description(read_file, headers_in_file):

    header_to_look_for = headers_in_file["description"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            description_in_file = row[header_to_look_for]
            row["description"] = description_in_file
    return read_file
