
def update_employee_name_id(read_file, headers_in_file):

    header_to_look_for = headers_in_file["employee_id"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            employee_id_in_file = row[header_to_look_for]
            row["employee_id"] = employee_id_in_file
    return read_file
