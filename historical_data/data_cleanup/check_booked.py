import datetime


def update_booked(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["booked"]
    for row in read_file:
        booked_in_file = row[header_to_look_for]
        row["booked"] = booked_in_file
    return read_file


# def _validate_date(date_text):
#     try:
#         if datetime.datetime.strptime(date_text, '%m/%d/%y'):
#             correct_formatted_date = datetime.datetime.strptime(date_text, '%m/%d/%y')
#             return correct_formatted_date
#         else:
#         correct_formatted_date = datetime.datetime.strptime(date_text, '%m/%d/%y')
#         return correct_formatted_date
#     except ValueError:
#         raise ValueError("Incorrect data format, should be MM/DD/YY")
