from tmc_templates.default import DefaultHistoricalFile


class CWTTemplate(DefaultHistoricalFile):

    def __init__(self):
        self.flight_headers = {
            "employee_name": "Traveler Name",
            "employee_id": "Client Defined 02",
            "organization": "",
            "fare_class": "Ticket Class Description",
            "vendor": "Validating Airline Name",
            "route": "Ticket Routing",
            "route_destinations": "",
            "route_destinations_city": "",
            "nonstop_or_connecting": "",
            "dom_or_int": "",
            "base_price": "Base Fare",
            "taxes_and_fees": "Tax",
            "total_price": "Paid Fare",
            "original_currency": "",
            "exchange_rate": "",
            "total_price_usd": "",
            "booked": "Issue Date",
            "ap_days": "Advance Purchase",
            "departure": "Ticket Departure Date",
            "return": "Ticket Return Date",
            "ticket_count": "",
            "department": "Client Defined 01",
            "in_pilot": "",
            "travel_group": "Issuing Country Code",
            "id": "",
            "ticket_number": "Ticket Number",
            "description": "RC Missed Global Description",
            "llf": "Lowest Fare Amount"
        }
        self.route_symbols = {
            "destination": " ",
            "connecting": ".",
            "openjaw": "/"
        }

