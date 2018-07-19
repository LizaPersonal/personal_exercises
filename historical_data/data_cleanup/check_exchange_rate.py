
def update_exchange_rate(read_file):
    for row in read_file:
        if row["original_currency"] == 'USD':
            row["exchange_rate"] = 1
        else:
            row["exchange_rate"] = _get_new_exchange_rate(row["original_currency"])
    return read_file


def _get_new_exchange_rate(original_currency):
    print(original_currency + """ is not USD.""")
    new_exchange_rate = input("What exchange rate should be used to convert to USD?")
    return new_exchange_rate
