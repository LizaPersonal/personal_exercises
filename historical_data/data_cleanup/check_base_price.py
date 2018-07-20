
def update_base_price(read_file, flight_headers_in_file):

    header_to_look_for = flight_headers_in_file["base_price"]
    for row in read_file:
        base_price_in_file = row[header_to_look_for]
        if base_price_in_file == "":
            row["base_price"] = base_price_in_file
        elif base_price_in_file is None:
            row["base_price"] = base_price_in_file
        else:
            base_price = check_price_format(base_price_in_file)
            row["base_price"] = base_price
    return read_file


def check_price_format(price):
    last_digit = len(price)-1
    price_is_negative = ""
    if price == '':
        formatted_price = 0.00
    else:
        if price[0] in ["(", "-"]:
            price_is_negative = "-"
        while not price[0].isdigit() and last_digit != 0:
            price = price[1:]
            last_digit -= 1
        while not price[last_digit].isdigit() and last_digit != 0:
            price = price[:-1]
            last_digit -= 1
        if price == ' ':
            formatted_price = 0.00
        else:
            if price_is_negative == "-":
                price = price_is_negative + price
            formatted_price = price.replace(',', '')
    return formatted_price
