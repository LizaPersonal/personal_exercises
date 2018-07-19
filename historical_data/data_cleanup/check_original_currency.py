
def update_original_currency(read_file, flight_headers_in_file):

    header_for_currency = flight_headers_in_file["original_currency"]
    header_for_base_price = flight_headers_in_file["base_price"]
    header_for_total_price = flight_headers_in_file["total_price"]
    for row in read_file:
        if header_for_currency != 'original_currency':
            currency_in_file = row[header_for_currency]
            if currency_in_file != '':
                row["original_currency"] = currency_in_file
        elif header_for_base_price != 'base_price':
            base_price_in_file = row[header_for_base_price]
            if base_price_in_file != '':
                price_currency = _get_currency_from_price(base_price_in_file)
                row["original_currency"] = price_currency
        elif header_for_total_price != 'total_price':
            total_price_in_file = row[header_for_total_price]
            if total_price_in_file != '':
                price_currency = _get_currency_from_price(total_price_in_file)
                row["original_currency"] = price_currency
        else:
            row["original_currency"] = 'USD'
    return read_file


def _get_currency_from_price(price):
    last_digit = len(price) - 1
    if not price[0].isdigit():
        if price[0] != ' ':
            price_currency = price[0]
    elif not price[last_digit].isdigit():
        price_currency = price[last_digit]
    return price_currency


def _find_currency_in_database(currency_symbol):
    pass
