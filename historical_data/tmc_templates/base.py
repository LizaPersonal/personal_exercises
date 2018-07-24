class BaseHistoricalFile(object):

    def __init__(self):
        self.flight_headers = ["employee_name",
                               "employee_id",
                               "organization",
                               "fare_class",
                               "vendor",
                               "route",
                               "route_destinations",
                               "route_destinations_city",
                               "nonstop_or_connecting",
                               "dom_or_int",
                               "base_price",
                               "taxes_and_fees",
                               "total_price",
                               "original_currency",
                               "exchange_rate",
                               "total_price_usd",
                               "booked",
                               "ap_days",
                               "departure",
                               "return",
                               "ticket_count",
                               "department",
                               "in_pilot",
                               "travel_group",
                               "ticket_number",
                               "description",
                               "llf"]
        self.hotel_headers = ["employee_name",
                              "employee_id",
                              "organization",
                              "room_type",
                              "hotel_brand",
                              "hotel_property",
                              "hotel_city",
                              "hotel_state_id",
                              "hotel_country_id",
                              "base_price",
                              "taxes_and_fees",
                              "total_price",
                              "original_currency",
                              "exchange_rate",
                              "base_price_usd",
                              "total_price_usd",
                              "room_rate_usd",
                              "booked",
                              "ap_days",
                              "checkin",
                              "checkout",
                              "hotel_nights",
                              "department",
                              "in_pilot",
                              "travel_group",
                              "ticket_number"]
        self.car_headers = ["employee_name",
                            "employee_id",
                            "organization",
                            "vehicle_type",
                            "vendor",
                            "pickup_city",
                            "pickup_state",
                            "pickup_country",
                            "base_price",
                            "taxes_and_fees",
                            "total_price",
                            "original_currency",
                            "exchange_rate",
                            "base_price_usd",
                            "total_price_usd",
                            "rental_rate_usd",
                            "booked",
                            "ap_days",
                            "pickup",
                            "dropoff",
                            "car_days",
                            "department",
                            "in_pilot",
                            "travel_group",
                            "ticket_number"]
        self.rail_headers = ["employee_name",
                             "employee_id",
                             "organization",
                             "fare_class",
                             "vendor",
                             "route",
                             "base_price",
                             "taxes_and_fees",
                             "total_price",
                             "original_currency",
                             "exchange_rate",
                             "total_price_usd",
                             "booked",
                             "ap_days",
                             "departure",
                             "return",
                             "ticket_count",
                             "department",
                             "in_pilot",
                             "travel_group",
                             "ticket_number"]
