from data_cleanup.check_airline_vendors import update_airline_vendor, _search_airline_database


def test_update_airline_vendor():
    assert update_airline_vendor()


def test_airline_in_database():
    assert _search_airline_database(cursor, "Delta") == "DL"


def test_airline_not_in_database():
    assert _search_airline_database(cursor, "Not Airline") is None


