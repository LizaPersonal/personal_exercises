import csv
from data_cleanup import check_connecting_vs_nonstop, check_airline_vendors, check_domestic_vs_international, \
    check_route, check_route_destinations, check_route_destinations_city, check_employee_name, check_fare_class, \
    check_employee_id, check_base_price, check_taxes_and_fees, check_total_price, check_original_currency, \
    check_exchange_rate, check_total_price_usd, check_llf, check_in_pilot, check_travel_group, check_ticket_number, \
    check_description, check_department, check_ticket_count, check_booked, check_departure, check_return, check_ap_days
from tmc_templates import default, base, cwt


def read_historical_data_file(file):
    """ Open a file and parse the headers and file content to be used later. """

    with open(file, "r", newline='') as historical_data_file:
        read_file = []
        reader = csv.DictReader(historical_data_file)
        headers = reader.fieldnames
        for row in reader:
            read_file.append(row)
    return headers, read_file


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
        tmc_template = default.DefaultFlights()
    elif tmc == 'cwt':
        tmc_template = cwt.CWTTemplate()
    else:
        print("That is not a valid TMC at this time.")
        return None
    return tmc_template


class HeaderProvider(object):

    def get_headers(self):
        result = base.BaseHistoricalFile().flight_headers
        return result


def compare_headers(flight_headers_from_file, tmc_template_flights, header_provider=HeaderProvider()):
    """ Review the headers from the file, and if there are any missing required headers for the output,
        add those additional headers to the file headers. """

    flight_headers_needed_in_output = header_provider.get_headers()

    for header in flight_headers_needed_in_output:
        if tmc_template_flights[header] == "":
            flight_headers_from_file.append(header)
            tmc_template_flights[header] = header


def update_organization(read_file, flight_headers_in_file, organization):
    """ Populate the organization column with the organization name provided by the user. """

    header_to_look_for = flight_headers_in_file["organization"]
    for row in read_file:
        row[header_to_look_for] = organization
    return read_file


# def update_headers(flight_headers_from_file, template_headers):
#
#     for needed_header in template_headers:
#         for index, header in enumerate(flight_headers_from_file):
#             if template_headers[needed_header] == header:
#                 flight_headers_from_file[index] = needed_header
#                 break
#     return flight_headers_from_file


def create_new_output_file(updated_file, header_provider=HeaderProvider()):
    """ Write to a new file all the changes made. """
    standard_headers = header_provider.get_headers()
    writer = csv.DictWriter(open('/tmp/output.csv', "w+"), fieldnames=standard_headers, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(updated_file)


if __name__== "__main__":

    filename = input("What file would you like to read? ")
    filename = "/Users/lizajohn/Documents/Clients/ServiceNow/International/GB_Air_Rocketrip_Extract_test.csv"
    template_to_use = validate_tmc()
    if template_to_use.route_symbols is None:
        destination_symbol = input("What symbol represents the destinations of the route in this file? ")
        connecting_symbol = input("What symbol represents the route is connecting in this file? ")
        openjaw_symbol = input("What symbol represents the route has an open jaw in this file? ")
    else:
        destination_symbol = template_to_use.route_symbols["destination"]
        connecting_symbol = template_to_use.route_symbols["connecting"]
        openjaw_symbol = template_to_use.route_symbols["openjaw"]

    # travel_mode = input("What type of travel are you looking to upload? ")

    organization_name = input("What is the name of the organization? ")
    default_currency = input("If there is no currency indicated, what should be used as the default? ")

    headers_after_reading, file_after_reading = read_historical_data_file(filename)
    compare_headers(headers_after_reading, template_to_use.flight_headers)

    updated_file = check_employee_name.update_employee_name(file_after_reading, template_to_use.flight_headers)
    print("\n"+u"\u2713"+" Employee Name                 3.7%")
    updated_file = check_employee_id.update_employee_name_id(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Employee ID                   7.4%")
    updated_file = update_organization(updated_file, template_to_use.flight_headers, organization_name)
    print(u"\u2713"+" Organization                  11.1%")
    # updated_file = check_fare_class.update_fare_class(updated_file, template_to_use.flight_headers)
    # print(u"\u2713"+" Fare Class                    14.8%")
    # updated_file = check_airline_vendors.update_airline_vendor(updated_file, template_to_use.flight_headers)
    # print(u"\u2713"+" Vendor                        18.5%")
    #
    # updated_file = check_route.updated_route(updated_file, template_to_use.flight_headers,
    #                                          destination_symbol, connecting_symbol, openjaw_symbol)
    # print(u"\u2713"+" Route                         22.2%")
    # updated_file = check_route_destinations.updated_route_destinations(updated_file)
    # print(u"\u2713"+" Route Destinations            25.9%")
    # updated_file = check_route_destinations_city.updated_route_destinations_city(updated_file)
    # print(u"\u2713"+" Route Destinations City       29.6%")
    # updated_file = check_connecting_vs_nonstop.update_connecting_vs_nonstop(updated_file)
    # print(u"\u2713"+" Non-stop vs. Connecting       33.3%")
    # updated_file = check_domestic_vs_international.updated_domestic_vs_international(updated_file)
    # print(u"\u2713"+" Domestic vs. International    37.0%")

    updated_file = check_base_price.update_base_price(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Base Price                    40.7%")
    updated_file = check_taxes_and_fees.update_taxes_and_fees(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Taxes and Fees                44.4%")
    updated_file = check_total_price.update_total_price(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Total Price                   48.1%")
    updated_file = check_original_currency.update_original_currency(updated_file, template_to_use.flight_headers, default_currency)
    print(u"\u2713"+" Currency                      51.8%")
    updated_file = check_exchange_rate.update_exchange_rate(updated_file)
    print(u"\u2713"+" Exchange Rate                 55.5%")
    updated_file = check_total_price_usd.update_total_price_usd(updated_file)
    print(u"\u2713"+" Total Price USD               59.2%")
    updated_file = check_llf.update_llf(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" LLF                           62.9%")

    updated_file = check_booked.update_booked(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Booked Date                   66.6%")
    updated_file = check_departure.update_departure(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Departure Date                70.3%")
    updated_file = check_return.update_return(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Return Date                   74.0%")
    updated_file = check_ap_days.update_ap_days(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" AP Days                       77.7%")

    updated_file = check_ticket_count.update_ticket_count(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Ticket Count                  81.4%")
    updated_file = check_department.update_department(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Department                    85.1%")
    updated_file = check_in_pilot.update_in_pilot(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" In Pilot                      88.8%")
    updated_file = check_travel_group.update_travel_group(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Travel Group                  92.5%")
    updated_file = check_ticket_number.update_ticket_number(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Ticket Number                 96.2%")
    updated_file = check_description.update_description(updated_file, template_to_use.flight_headers)
    print(u"\u2713"+" Description                   100%")

    create_new_output_file(updated_file)
