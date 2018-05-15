import csv
from data_cleanup import check_connecting_vs_nonstop, check_airline_vendors, check_domestic_vs_international
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
        return default_tmc_flight_headers.flight_headers
    else:
        print("That is not a valid TMC at this time.")
        return None


def validate_airline(read_file, flight_headers_in_file):
    """ Identify which column represents the vendor.
        For each row search in the database in the airlines table for the vendor code.
        Update the file with the vendor code rather than vendor name. """

    header_to_look_for = flight_headers_in_file["vendor"]
    for row in read_file:
        airline_in_file = row[header_to_look_for]
        vendor_code = check_airline_vendors.validate_airline_vendor((airline_in_file, ))
        row[header_to_look_for] = vendor_code[0]
    return read_file


def validate_connecting_vs_nonstop(read_file, flight_headers_in_file):
    """ Identify which column represents the route and the nonstop/connecting.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_to_look_for = flight_headers_in_file["route"]
    header_to_update = flight_headers_in_file["nonstop_or_connecting"]
    for row in read_file:
        route = row[header_to_look_for]
        nonstop_connecting = check_connecting_vs_nonstop.nonstop_or_connecting(route)
        row[header_to_update] = nonstop_connecting
    return read_file


def validate_domestic_vs_international(read_file, flight_headers_in_file):
    """ Identify which column represents the route and the domestic/international.
        For each row identify if the route is nonstop or connecting.
        Update the file with the correcting indication in the nonstop/connecting column. """

    header_to_look_for = flight_headers_in_file["route"]
    header_to_update = flight_headers_in_file["dom_or_int"]
    for row in read_file:
        route = row[header_to_look_for]
        domestic_international = check_domestic_vs_international.domestic_or_international(route)
        row[header_to_update] = domestic_international
    return read_file


def create_new_output_file(updated_file, fields):
    """ Write to a new file all the changes made. """
    writer = csv.DictWriter(open('/tmp/output.csv', "w+"), fieldnames=fields)
    writer.writeheader()
    writer.writerows(updated_file)


if __name__== "__main__":

    filename = input("What file would you like to read? ")
    filename = "/Users/lizajohn/Documents/Historical_Data_Request_Template_copy.csv"
    flight_headers = validate_tmc()

    # travel_mode = input("What type of travel are you looking to upload? ")
    #
    # organization_name = input("What is the name of the organization? ")

    headers_after_reading, file_after_reading = read_historical_data_file(filename)
    updated_airlines = validate_airline(file_after_reading, flight_headers)
    updated_connecting_vs_nonstop = validate_connecting_vs_nonstop(updated_airlines, flight_headers)
    updated_domestic_vs_international = validate_domestic_vs_international(updated_connecting_vs_nonstop, flight_headers)
    create_new_output_file(updated_connecting_vs_nonstop, headers_after_reading)

