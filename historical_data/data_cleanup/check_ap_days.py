from datetime import datetime


def update_ap_days(read_file, headers_in_file, travel_type):

    header_to_look_for = headers_in_file["ap_days"]

    for row in read_file:
        if travel_type == "flight":
            leave_date_in_file = row["departure"]
        elif travel_type == "hotel":
            leave_date_in_file = row["checkout"]
        booked_in_file = row["booked"]
        if row.get(header_to_look_for) is not None:
            ap_days_in_file = row["ap_days"]
            if ap_days_in_file != "":
                row["ap_days"] = ap_days_in_file
            elif booked_in_file != "" and leave_date_in_file != "":
                ap_days = datetime.strptime(leave_date_in_file, '%m/%d/%y') - datetime.strptime(booked_in_file, '%m/%d/%y')
                row["ap_days"] = ap_days.days
            else:
                row["ap_days"] = "NULL"
        else:
            if booked_in_file != "" and leave_date_in_file != "":
                ap_days = datetime.strptime(leave_date_in_file, '%m/%d/%y') - datetime.strptime(booked_in_file, '%m/%d/%y')
                row["ap_days"] = ap_days.days
            else:
                row["ap_days"] = "NULL"
    return read_file
