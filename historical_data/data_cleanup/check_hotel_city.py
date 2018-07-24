from data_cleanup.check_employee_name import set_name_to_correct_case


def update_hotel_city(read_file, headers_in_file):

    header_to_look_for = headers_in_file["hotel_city"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            hotel_city_in_file = row[header_to_look_for]
            formatted_hotel_city = set_name_to_correct_case(hotel_city_in_file)
            row["hotel_city"] = formatted_hotel_city
    return read_file
