
class DefaultHistoricalFile(object):

    def __init__(self):
        self.flight_headers = {}
        self.hotel_headers = []
        self.car_headers = []
        self.rail_headers = []


class DefaultFlights(DefaultHistoricalFile):

    def __init__(self):
        self.flight_headers = {
            "employee_name": "Employee Name",
            "employee_id": "Employee ID",
            "organization": "",
            "fare_class": "Fare Class",
            "vendor": "Vendor *",
            "route": "Route",
            "route_destinations": "",
            "route_destinations_city": "",
            "nonstop_or_connecting": "Connecting vs Nonstop *",
            "dom_or_int": "Domestic vs International *",
            "base_price": "Base Price",
            "taxes_and_fees": "Taxes and Fees",
            "total_price": "Total Price",
            "original_currency": "Original Currency",
            "exchange_rate": "",
            "total_price_usd": "",
            "booked": "Booking Date",
            "ap_days": "Days Purchased in Advance",
            "departure": "Departure Date",
            "return": "Return Date",
            "ticket_count": "Ticket Count",
            "department": "Employee Department",
            "in_pilot": "",
            "travel_group": "",
            "id": "",
            "ticket_number": "Ticket Number",
            "description": "LLA/LLF Chosen",
            "llf": "Low Fare"
        }


class DefaultHotels(DefaultHistoricalFile):
    pass


class DefaultCars(DefaultHistoricalFile):
    pass


class DefaultRail(DefaultHistoricalFile):
    pass