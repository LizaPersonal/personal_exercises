from datetime import datetime


def update_ap_days(read_file, headers_in_file, travel_type):

    header_to_look_for = headers_in_file["ap_days"]

    for row in read_file:
        if travel_type == "flight":
            leave_date_in_file = row["departure"]
        elif travel_type == "hotel":
            leave_date_in_file = row["checkin"]
        booked_in_file = row["booked"]
        if row.get(header_to_look_for) is not None:
            ap_days_in_file = row[header_to_look_for]
            if ap_days_in_file != "" and int(ap_days_in_file):
                row["ap_days"] = ap_days_in_file
            else:
                row["ap_days"] = _calculate_ap_days(booked_in_file, leave_date_in_file)
        else:
            row["ap_days"] = _calculate_ap_days(booked_in_file, leave_date_in_file)
    return read_file


def _calculate_ap_days(booked, leave):
    if booked != "" and leave != "":
        ap_days = datetime.strptime(leave, '%m/%d/%y') - datetime.strptime(booked, '%m/%d/%y')
        result = ap_days.days
    else:
        result = "NULL"
    return result
