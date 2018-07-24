
def update_ap_days(read_file, headers_in_file):

    header_for_ap_days = headers_in_file["ap_days"]

    for row in read_file:
        ap_days_in_file = row[header_for_ap_days]
        booked_in_file = row["booked"]
        departure_in_file = row["departure"]
        if ap_days_in_file != "":
            row["ap_days"] = ap_days_in_file
        elif booked_in_file != "" and departure_in_file != "":
            ap_days = departure_in_file - booked_in_file
            row["ap_days"] = ap_days
        else:
            row["ap_days"] = "NULL"
    return read_file
