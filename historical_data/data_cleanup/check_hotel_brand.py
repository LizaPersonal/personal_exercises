from data_cleanup.check_employee_name import set_name_to_correct_case


def update_hotel_brand(read_file, headers_in_file):

    header_to_look_for = headers_in_file["hotel_brand"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            hotel_brand_in_file = row[header_to_look_for]
            formatted_hotel_brand = set_name_to_correct_case(hotel_brand_in_file)
            row["hotel_brand"] = formatted_hotel_brand
    return read_file
