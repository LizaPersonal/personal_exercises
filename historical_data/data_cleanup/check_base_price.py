
def update_base_price(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["base_price"]
    for row in read_file:
        base_price_in_file = row[header_to_look_for]
        base_price = check_price_format(base_price_in_file)
        row["base_price"] = base_price
    return read_file


def check_price_format(price):
    last_digit = len(price)-1
    while not price[0].isdigit():
        price = price[1:]
        last_digit -= 1
    while not price[last_digit].isdigit():
        price = price[:-1]
        last_digit -= 1
    formatted_price = price.replace(',', '')
    return formatted_price