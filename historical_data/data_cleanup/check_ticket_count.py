
def update_ticket_count(read_file, headers_in_file):

    header_to_look_for = headers_in_file["ticket_count"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            ticket_count_in_file = row[header_to_look_for]
            if ticket_count_in_file != "" and type(ticket_count_in_file) is int:
                row["ticket_count"] = ticket_count_in_file
            else:
                row["ticket_count"] = 1
        else:
            row["ticket_count"] = 1
    return read_file
