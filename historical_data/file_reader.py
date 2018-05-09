import csv
# from tmc_templates.default import DefaultFlights
# from historical_data import check_airline_vendors, check_connecting_vs_nonstop
from data_cleanup import check_connecting_vs_nonstop, check_airline_vendors
from tmc_templates.default import DefaultFlights


class GeneralError(Exception):
    pass


class NotValidFile(Exception):
    pass


def read_historical_data_file(file):
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
    tmc = input("Which TMC is the file from? ")
    if _tmc_template_to_use(tmc) is None:
        validate_tmc()
    else:
        return _tmc_template_to_use(tmc)


def _tmc_template_to_use(tmc):
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
    header_to_look_for = flight_headers_in_file["vendor"]
    for row in read_file:
        airline_in_file = row[header_to_look_for]
        vendor_code = check_airline_vendors.validate_airline_vendor((airline_in_file, ))
        row[header_to_look_for] = vendor_code[0]
    return read_file


def validate_connecting_vs_nonstop(read_file, flight_headers_in_file):
    header_to_look_for = flight_headers_in_file["route"]
    header_to_update = flight_headers_in_file["nonstop_or_connecting"]
    for row in read_file:
        route_type = row[header_to_look_for]
        nonstop_connecting = check_connecting_vs_nonstop.nonstop_or_connecting(route_type)
        row[header_to_update] = nonstop_connecting
    return read_file


def create_new_output_file(updated_file, fields):
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
    create_new_output_file(updated_connecting_vs_nonstop, headers_after_reading)

