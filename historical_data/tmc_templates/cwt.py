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
            "base_price": " Base Fare ",
            "taxes_and_fees": " Tax ",
            "total_price": " Paid Fare ",
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
            "llf": " Lowest Fare Amount "
        }
        self.route_symbols = {
            "destination": " ",
            "connecting": ".",
            "openjaw": "/"
        }
        self.hotel_headers = {
            "employee_name": "Traveler Name",
            "employee_id": "Client Defined 02",
            "organization": "",
            "room_type": "Room Type",
            "hotel_brand": "Hotel Chain Name",
            "hotel_property": "Property Name",
            "hotel_city": "Hotel City",
            "hotel_state": "Hotel State",
            "hotel_country": "Hotel Country",
            "base_price": "",
            "taxes_and_fees": "",
            "total_price": " Total Hotel Cost ",
            "original_currency": "",
            "exchange_rate": "",
            "base_price_usd": "",
            "total_price_usd": "",
            "room_rate_usd": " Room Rate ",
            "booked": "Issue Date",
            "ap_days": "",
            "checkin": "In Date",
            "checkout": "Out Date",
            "hotel_nights": "Room Nights",
            "department": "Client Defined 01",
            "in_pilot": "",
            "travel_group": "Issuing Country Name",
            "ticket_number": ""}

