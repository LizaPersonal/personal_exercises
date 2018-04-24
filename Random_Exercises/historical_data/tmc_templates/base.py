class BaseHistoricalFile(object):

    def __init__(self):
        self.headers = []

    def append_organization_name(self):
        pass

    def calculate_route_destinations(self):
        pass

    def calculate_route_destinations_city(self):
        pass

    def additional_fields(self):
        extra_fields = [organization_name,
                        route_desinations,
                        route_desinations_city,
                        exchange_rate,
                        total_price_usd]