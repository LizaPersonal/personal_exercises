from data_cleanup.check_employee_name import set_name_to_correct_case


def update_travel_group(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["travel_group"]
    for row in read_file:
        travel_group_in_file = row[header_to_look_for]
        formatted_travel_group = set_name_to_correct_case(travel_group_in_file)
        row["travel_group"] = formatted_travel_group
    return read_file
