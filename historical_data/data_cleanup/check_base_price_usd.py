
def update_base_price_usd(read_file):

    for row in read_file:
        if row.get("base_price") is not None:
            if row["exchange_rate"] == 1:
                row["base_price_usd"] = row["base_price"]
            else:
                row["base_price_usd"] = float(row["base_price"]) * float(row["exchange_rate"])
    return read_file
