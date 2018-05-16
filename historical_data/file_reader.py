import csv
from data_cleanup import check_connecting_vs_nonstop, check_airline_vendors, check_domestic_vs_international, check_route
from tmc_templates.default import DefaultFlights


class GeneralError(Exception):
    pass


class NotValidFile(Exception):
    pass


def read_historical_data_file(file):
    """ Open a file and parse the headers and file content to be used later. """

    if file is None:
        raise GeneralError()
    with open(file, "r", newline='') as historical_data_file:
        read_file = []
        reader = csv.DictReader(historical_data_file)
        headers = reader.fieldnames
        for row in reader:
            read_file.append(row)
    return headers, read_file


# def print_historical_csv(read_file):
#     for row in read_file:
#         print(row)

def validate_tmc():
    """ Ask the user for the tmc, and validate we have a mapping for them. """

    tmc = input("Which TMC is the file from? ")
    tmc_template_exists = _tmc_template_to_use(tmc)
    if tmc_template_exists is None:
        validate_tmc()
    else:
        return tmc_template_exists


def _tmc_template_to_use(tmc):
    """ Identify which template headers should be used based on the user input. """

    if tmc == 'default':
        default_tmc_flight_headers = DefaultFlights()
        # default_tmc_flight_headers = {"vendor": "Vendor *",
        #                               "route": "Route",
        #                               "nonstop_or_connecting": "Connecting vs Nonstop *"}
        return default_tmc_flight_headers.flight_headers, default_tmc_flight_headers.route_symbols
    else:
        print("That is not a valid TMC at this time.")
        return None


def update_organization(read_file, flight_headers_in_file, organization_name):
    """ Populate the organization column with the organization name provided by the user. """

    header_to_look_for = flight_headers_in_file["organization"]
    for row in read_file:
        row[header_to_look_for] = organization_name
    return read_file


def create_new_output_file(updated_file, fields):
    """ Write to a new file all the changes made. """
    writer = csv.DictWriter(open('/tmp/output.csv', "w+"), fieldnames=fields)
    writer.writeheader()
    writer.writerows(updated_file)


if __name__== "__main__":

    filename = input("What file would you like to read? ")
    filename = "/Users/lizajohn/Documents/Historical_Data_Request_Template_copy.csv"
    flight_headers, route_symbols = validate_tmc()
    if route_symbols is None:
        destination_symbol = input("What symbol represents the destinations of the route in this file?")
        connecting_symbol = input("What symbol represents the route is connecting in this file?")
        openjaw_symbol = input("What symbol represents the route has an open jaw in this file?")
    else:
        destination_symbol = route_symbols["destination"]
        connecting_symbol = route_symbols["connecting"]
        openjaw_symbol = route_symbols["openjaw"]

    # travel_mode = input("What type of travel are you looking to upload? ")
    #
    # organization_name = input("What is the name of the organization? ")

    headers_after_reading, file_after_reading = read_historical_data_file(filename)
    updated_airlines = check_airline_vendors.update_airline_vendor(file_after_reading, flight_headers)
    updated_route = check_route.updated_route(updated_airlines, flight_headers, destination_symbol, connecting_symbol, openjaw_symbol)
    updated_connecting_vs_nonstop = check_connecting_vs_nonstop.update_connecting_vs_nonstop(updated_route, flight_headers)
    updated_domestic_vs_international = check_domestic_vs_international.updated_domestic_vs_international(updated_connecting_vs_nonstop, flight_headers)
    # updated_organization_column = update_organization(updated_domestic_vs_international, flight_headers, organization_name)
    create_new_output_file(updated_domestic_vs_international, headers_after_reading)

