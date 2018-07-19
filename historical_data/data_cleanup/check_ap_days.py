
def update_ap_days(read_file, flight_headers_in_file):

    header_for_ap_days = flight_headers_in_file["ap_days"]

    for row in read_file:
        ap_days_in_file = row[header_for_ap_days]
        booked_in_file = row['booked']
        departure_in_file = row['departure']
        if ap_days_in_file != "":
            row["ap_days"] = ap_days_in_file
        else:
            ap_days = departure_in_file - booked_in_file
            row["ap_days"] = ap_days
    return read_file
