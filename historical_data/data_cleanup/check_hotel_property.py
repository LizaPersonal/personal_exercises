from data_cleanup.check_employee_name import set_name_to_correct_case


def update_hotel_property(read_file, headers_in_file):

    header_to_look_for = headers_in_file["hotel_property"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            property_in_file = row[header_to_look_for]
            formatted_property = set_name_to_correct_case(property_in_file)
            row["hotel_property"] = formatted_property
    return read_file
