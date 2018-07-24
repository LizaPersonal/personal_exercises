from data_cleanup.check_base_price import check_price_format


def update_room_rate_usd(read_file, headers_in_file):

    header_for_room_rate = headers_in_file["room_rate_usd"]
    header_for_base_price_usd = headers_in_file["base_price_usd"]
    header_for_hotel_nights = headers_in_file["hotel_nights"]
    header_for_total_price_usd = headers_in_file["total_price_usd"]

    for row in read_file:
        if row.get(header_for_room_rate) is not None:
            room_rate_in_file = row[header_for_room_rate]
            if room_rate_in_file != "":
                room_rate = check_price_format(room_rate_in_file)
            elif row.get(header_for_base_price_usd) is not None and row.get(header_for_hotel_nights) is not None:
                base_price_in_file = row[header_for_base_price_usd]
                hotel_nights_in_file = row[header_for_hotel_nights]
                room_rate = float(base_price_in_file) / float(hotel_nights_in_file)
            elif row.get(header_for_total_price_usd) is not None and row.get(header_for_hotel_nights) is not None:
                total_price_in_file = row[header_for_total_price_usd]
                hotel_nights_in_file = row[header_for_hotel_nights]
                room_rate = float(total_price_in_file) / float(hotel_nights_in_file)
            else:
                room_rate = 0.00
            row["room_rate_usd"] = room_rate
    return read_file
