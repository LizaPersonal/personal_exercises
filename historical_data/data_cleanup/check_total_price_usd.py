
def update_total_price_usd(read_file):

    for row in read_file:
        if row.get("total_price") is not None:
            row["total_price_usd"] = float(row["total_price"]) * float(row["exchange_rate"])
    return read_file
