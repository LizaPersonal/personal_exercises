
def update_hotel_nights(read_file, headers_in_file):

    header_for_hotel_nights = headers_in_file["hotel_nights"]

    for row in read_file:
        hotel_nights_in_file = row[header_for_hotel_nights]
        booked_in_file = row["booked"]
        checkin_in_file = row["checkin"]
        if hotel_nights_in_file != "":
            row["hotel_nights"] = hotel_nights_in_file
        elif booked_in_file != "" and checkin_in_file != "":
            ap_days = checkin_in_file - booked_in_file
            row["hotel_nights"] = ap_days
        else:
            row["hotel_nights"] = "NULL"
    return read_file
