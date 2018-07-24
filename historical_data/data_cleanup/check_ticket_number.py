
def update_ticket_number(read_file, headers_in_file):

    header_to_look_for = headers_in_file["ticket_number"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            ticket_number_in_file = row[header_to_look_for]
            row["ticket_number"] = ticket_number_in_file
    return read_file
