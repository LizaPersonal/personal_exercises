from .base import BaseHistoricalFile


class DefaultHistoricalFile(BaseHistoricalFile):
    pass


class DefaultFlights(DefaultHistoricalFile):
    FIELDS_MAPPING = {
        "Record ID": "ticket_number",
        "Employee Name": "employee_name",
        "Employee ID": "employee_id",
        "Employee Email": "",
        "Employee Department": "",
        "Ticket Number": "",
        "Booking Date": "",
        "Vendor": "vendor",
        "Route": "route",
        "Connecting vs Nonstop": "nonstop_or_connecting",
        "Trip Type": "",
        "Departure Date": "",
        "Return Date": "",
        "Days Purchased in Advance": "",
        "Ticket Count": "",
        "Domestic vs International": "dom_or_int",
        "Fare Class": "fare_class",
        "Base Price": "base_price",
        "Taxes and Fees": "taxes_and_fees",
        "Original Currency": "original_currency",
        "Total Price": "total_price",
        "LLA/LLF Chosen": "",
        "Low Fare": "",
    }


class DefaultHotels(DefaultHistoricalFile):
    pass


class DefaultCars(DefaultHistoricalFile):
    pass


class DefaultRail(DefaultHistoricalFile):
    pass