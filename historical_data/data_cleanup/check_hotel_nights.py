from datetime import datetime


def update_hotel_nights(read_file, headers_in_file):

    header_for_hotel_nights = headers_in_file["hotel_nights"]

    for row in read_file:
        checkout_in_file = row["checkout"]
        checkin_in_file = row["checkin"]
        if row.get(header_for_hotel_nights) is not None:
            hotel_nights_in_file = row[header_for_hotel_nights]
            if hotel_nights_in_file != "":
                row["hotel_nights"] = hotel_nights_in_file
            elif checkout_in_file != "" and checkin_in_file != "":
                hotel_nights = datetime.strptime(checkout_in_file, '%m/%d/%y') - datetime.strptime(checkin_in_file, '%m/%d/%y')
                row["hotel_nights"] = hotel_nights
            else:
                row["hotel_nights"] = "NULL"
        else:
            if checkout_in_file != "" and checkin_in_file != "":
                hotel_nights = datetime.strptime(checkout_in_file, '%m/%d/%y') - datetime.strptime(checkin_in_file, '%m/%d/%y')
                row["hotel_nights"] = hotel_nights.days
            else:
                row["hotel_nights"] = "NULL"
    return read_file
