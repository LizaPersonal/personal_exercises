import datetime


def update_booked(read_file, headers_in_file):

    header_to_look_for = headers_in_file["booked"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            booked_in_file = row[header_to_look_for]
            formatted_booked = validate_date(booked_in_file)
            row["booked"] = formatted_booked
    return read_file


def validate_date(date_text):
    correct_formatted_date = ''
    if date_text == '':
        correct_formatted_date = ''
    else:
        if datetime.datetime.strptime(date_text, '%m/%d/%y'):
            correct_formatted_date = date_text
        elif datetime.datetime.strptime(date_text, '%d/%m/%y'):
            correct_formatted_date = datetime.datetime.strptime(date_text, '%d/%m/%y').strftime('%m/%d/%y')
    return correct_formatted_date
