
def update_total_price_usd(read_file):

    for row in read_file:
        if row["exchange_rate"] == 1:
            row["total_price_usd"] = row["total_price"]
        else:
            row["total_price_usd"] = float(row["total_price"]) * float(row["exchange_rate"])
    return read_file
