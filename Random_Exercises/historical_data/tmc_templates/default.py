from .base import BaseHistoricalFile


class DefaultHistoricalFile(BaseHistoricalFile):
    pass


class DefaultFlights(DefaultHistoricalFile):
    FIELDS_MAPPING = {
        "Record ID": "",
        "Employee Name": "employee_name",
        "Employee ID": "employee_id",
        "Employee Email": "",
        "Employee Department": "department",
        "Ticket Number": "ticket_number",
        "Booking Date": "booked",
        "Vendor": "vendor",
        "Route": "route",
        "Connecting vs Nonstop": "nonstop_or_connecting",
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
        "Low Fare": "llf",
    }


class DefaultHotels(DefaultHistoricalFile):
    pass


class DefaultCars(DefaultHistoricalFile):
    pass


class DefaultRail(DefaultHistoricalFile):
    pass