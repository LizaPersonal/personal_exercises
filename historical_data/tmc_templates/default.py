
class DefaultHistoricalFile(object):

    def __init__(self):
        self.flight_headers = {}
        self.hotel_headers = []
        self.car_headers = []
        self.rail_headers = []


class DefaultFlights(DefaultHistoricalFile):

    def __init__(self):
        self.flight_headers = {
            "Record ID": "",
            "Employee Name": "employee_name",
            "Employee ID": "employee_id",
            "Employee Email": "",
            "Employee Department": "department",
            "Ticket Number": "ticket_number",
            "Booking Date": "booked",
            "vendor": "Vendor *",
            "route": "Route",
            "nonstop_or_connecting": "Connecting vs Nonstop *",
            "Trip Type": "",
            "Departure Date": "departure",
            "Return Date": "return",
            "Days Purchased in Advance": "ap_days",
            "Ticket Count": "ticket_count",
            "Domestic vs International": "dom_or_int",
            "Fare Class": "fare_class",
            "Base Price": "base_price",
            "Taxes and Fees": "taxes_and_fees",
            "Original Currency": "original_currency",
            "Total Price": "total_price",
            "LLA/LLF Chosen": "description",
            "Low Fare": "llf"
        }


class DefaultHotels(DefaultHistoricalFile):
    pass


class DefaultCars(DefaultHistoricalFile):
    pass


class DefaultRail(DefaultHistoricalFile):
    pass