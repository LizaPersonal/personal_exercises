import csv
from data_cleanup import check_connecting_vs_nonstop, check_airline_vendors, check_domestic_vs_international, \
    check_route, check_route_destinations, check_route_destinations_city, check_employee_name, check_fare_class, \
    check_employee_id, check_base_price, check_taxes_and_fees, check_total_price, check_original_currency, \
    check_exchange_rate, check_total_price_usd, check_llf, check_in_pilot, check_travel_group, check_ticket_number, \
    check_description, check_department, check_ticket_count, check_booked, check_departure, \
    check_return, check_ap_days, check_room_type, check_base_price_usd, check_checkin, check_checkout, \
    check_hotel_nights, check_room_rate_usd
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
        tmc_template = default.DefaultTemplate()
    elif tmc == 'cwt':
        tmc_template = cwt.CWTTemplate()
    else:
        print("That is not a valid TMC at this time.")
        return None
    return tmc_template


def validate_travel_mode():

    travel_type = input("What type of travel are you looking to upload? ")
    if travel_type is None:
        validate_travel_mode()
    elif travel_type in ["flight", "hotel"]:
        return travel_type
    else:
        print("That is not a valid travel mode at this time.")
        validate_travel_mode()


class HeaderProvider(object):

    def get_flight_headers(self):
        result = base.BaseHistoricalFile().flight_headers
        return result

    def get_hotel_headers(self):
        result = base.BaseHistoricalFile().hotel_headers
        return result


def compare_headers(headers_from_file, tmc_template, travel_type, header_provider=HeaderProvider()):
    """ Review the headers from the file, and if there are any missing required headers for the output,
        add those additional headers to the file headers. """

    if travel_type == "flight":
        headers_needed_in_output = header_provider.get_flight_headers()
    elif travel_type == "hotel":
        headers_needed_in_output = header_provider.get_hotel_headers()

    for header in headers_needed_in_output:
        if tmc_template[header] == "":
            headers_from_file.append(header)
            tmc_template[header] = header


def update_organization(read_file, headers_in_file, organization):
    """ Populate the organization column with the organization name provided by the user. """

    header_to_look_for = headers_in_file["organization"]
    for row in read_file:
        row[header_to_look_for] = organization
    return read_file


def create_new_output_file(updated_file, travel_type, header_provider=HeaderProvider()):
    """ Write to a new file all the changes made. """

    if travel_type == "flight":
        standard_headers = header_provider.get_flight_headers()
    elif travel_type == "hotel":
        standard_headers = header_provider.get_hotel_headers()

    writer = csv.DictWriter(open('/tmp/output.csv', "w+"), fieldnames=standard_headers, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(updated_file)


def clean_flight_data(file, flight_headers, organization, destination, connecting, openjaw, currency):

    updated_file = check_employee_name.update_employee_name(file,flight_headers)
    print("\n"+u"\u2713"+" Employee Name                 3.7%")
    updated_file = check_employee_id.update_employee_name_id(updated_file, flight_headers)
    print(u"\u2713"+" Employee ID                   7.4%")
    updated_file = update_organization(updated_file, flight_headers, organization)
    print(u"\u2713"+" Organization                  11.1%")
    updated_file = check_fare_class.update_fare_class(updated_file, flight_headers)
    print(u"\u2713"+" Fare Class                    14.8%")
    updated_file = check_airline_vendors.update_airline_vendor(updated_file, flight_headers)
    print(u"\u2713"+" Vendor                        18.5%")

    updated_file = check_route.updated_route(updated_file, flight_headers, destination, connecting, openjaw)
    print(u"\u2713"+" Route                         22.2%")
    updated_file = check_route_destinations.updated_route_destinations(updated_file)
    print(u"\u2713"+" Route Destinations            25.9%")
    updated_file = check_route_destinations_city.updated_route_destinations_city(updated_file)
    print(u"\u2713"+" Route Destinations City       29.6%")
    updated_file = check_connecting_vs_nonstop.update_connecting_vs_nonstop(updated_file)
    print(u"\u2713"+" Non-stop vs. Connecting       33.3%")
    updated_file = check_domestic_vs_international.updated_domestic_vs_international(updated_file)
    print(u"\u2713"+" Domestic vs. International    37.0%")

    updated_file = check_base_price.update_base_price(updated_file, flight_headers)
    print(u"\u2713"+" Base Price                    40.7%")
    updated_file = check_taxes_and_fees.update_taxes_and_fees(updated_file, flight_headers)
    print(u"\u2713"+" Taxes and Fees                44.4%")
    updated_file = check_total_price.update_total_price(updated_file, flight_headers)
    print(u"\u2713"+" Total Price                   48.1%")
    updated_file = check_original_currency.update_original_currency(updated_file, flight_headers, currency)
    print(u"\u2713"+" Currency                      51.8%")
    updated_file = check_exchange_rate.update_exchange_rate(updated_file)
    print(u"\u2713"+" Exchange Rate                 55.5%")
    updated_file = check_total_price_usd.update_total_price_usd(updated_file)
    print(u"\u2713"+" Total Price USD               59.2%")

    updated_file = check_booked.update_booked(updated_file, flight_headers)
    print(u"\u2713"+" Booked Date                   66.6%")
    updated_file = check_departure.update_departure(updated_file, flight_headers)
    print(u"\u2713"+" Departure Date                70.3%")
    updated_file = check_return.update_return(updated_file, flight_headers)
    print(u"\u2713"+" Return Date                   74.0%")
    updated_file = check_ap_days.update_ap_days(updated_file)
    print(u"\u2713"+" AP Days                       77.7%")

    updated_file = check_ticket_count.update_ticket_count(updated_file, flight_headers)
    print(u"\u2713"+" Ticket Count                  81.4%")
    updated_file = check_department.update_department(updated_file, flight_headers)
    print(u"\u2713"+" Department                    85.1%")
    updated_file = check_in_pilot.update_in_pilot(updated_file, flight_headers)
    print(u"\u2713"+" In Pilot                      88.8%")
    updated_file = check_travel_group.update_travel_group(updated_file, flight_headers)
    print(u"\u2713"+" Travel Group                  92.5%")
    updated_file = check_ticket_number.update_ticket_number(updated_file, flight_headers)
    print(u"\u2713"+" Ticket Number                 96.2%")
    updated_file = check_description.update_description(updated_file, flight_headers)
    print(u"\u2713"+" Description                   100%")

    return updated_file


def clean_hotel_data(file, hotel_headers, organization, currency):

    updated_file = check_employee_name.update_employee_name(file, hotel_headers)
    print("\n" + u"\u2713" + " Employee Name                 3.8%")
    updated_file = check_employee_id.update_employee_name_id(updated_file, hotel_headers)
    print(u"\u2713" + " Employee ID                   7.6%")
    updated_file = update_organization(updated_file, hotel_headers, organization)
    print(u"\u2713" + " Organization                  11.4%")

    updated_file = check_room_type.update_room_type(updated_file, hotel_headers)
    print(u"\u2713" + " Room Type                     15.2%")
    print(u"\u2713" + " Hotel Brand                   19.0%")
    print(u"\u2713" + " Hotel Property                22.8%")
    print(u"\u2713" + " Hotel City                    26.6%")
    print(u"\u2713" + " Hotel State                   30.4%")
    print(u"\u2713" + " Hotel Country                 34.2%")

    updated_file = check_base_price.update_base_price(updated_file, hotel_headers)
    print(u"\u2713" + " Base Price                    38.0%")
    updated_file = check_taxes_and_fees.update_taxes_and_fees(updated_file, hotel_headers)
    print(u"\u2713" + " Taxes and Fees                41.8%")
    updated_file = check_total_price.update_total_price(updated_file, hotel_headers)
    print(u"\u2713" + " Total Price                   45.6%")
    updated_file = check_original_currency.update_original_currency(updated_file, hotel_headers, currency)
    print(u"\u2713" + " Currency                      49.4%")
    updated_file = check_exchange_rate.update_exchange_rate(updated_file)
    print(u"\u2713" + " Exchange Rate                 53.2%")
    updated_file = check_base_price_usd.update_base_price_usd(updated_file)
    print(u"\u2713" + " Base Price USD                57.0%")
    updated_file = check_total_price_usd.update_total_price_usd(updated_file)
    print(u"\u2713" + " Total Price USD               60.8%")

    updated_file = check_booked.update_booked(updated_file,hotel_headers)
    print(u"\u2713" + " Booked Date                   64.6%")
    updated_file = check_checkin.update_checkin(updated_file, hotel_headers)
    print(u"\u2713" + " Check-in Date                 68.4%")
    updated_file = check_checkout.update_checkout(updated_file, hotel_headers)
    print(u"\u2713" + " Check-out Date                72.2%")
    updated_file = check_ap_days.update_ap_days(updated_file)
    print(u"\u2713" + " AP Date                       76.0%")

    updated_file = check_hotel_nights.update_hotel_nights(updated_file, hotel_headers)
    print(u"\u2713" + " Hotel Nights                  79.8%")
    updated_file = check_room_rate_usd.update_room_rate_usd(updated_file, hotel_headers)
    print(u"\u2713" + " Room Rate USD                 83.6%")

    updated_file = check_department.update_department(updated_file, hotel_headers)
    print(u"\u2713" + " Department                    87.4%")
    updated_file = check_in_pilot.update_in_pilot(updated_file, hotel_headers)
    print(u"\u2713" + " In Pilot                      91.2%")
    updated_file = check_travel_group.update_travel_group(updated_file, hotel_headers)
    print(u"\u2713" + " Travel Group                  95.0%")
    updated_file = check_ticket_number.update_ticket_number(updated_file, hotel_headers)
    print(u"\u2713" + " Ticket Number                 100%")

    return updated_file


if __name__== "__main__":

    filename = input("What file would you like to read? ")
    # filename = "/Users/lizajohn/Documents/Clients/ServiceNow/International/AU_Hotel_Rocketrip_Extract.csv"
    # filename = "/Users/lizajohn/Documents/CWT_Flight_Template_test.csv"
    filename = "/Users/lizajohn/Documents/CWT_Hotel_Template_test.csv"
    template_to_use = validate_tmc()
    travel_mode = validate_travel_mode()

    if travel_mode == "flight" and template_to_use.route_symbols is None:
        destination_symbol = input("What symbol represents the destinations of the route in this file? ")
        connecting_symbol = input("What symbol represents the route is connecting in this file? ")
        openjaw_symbol = input("What symbol represents the route has an open jaw in this file? ")
    elif travel_mode == "flight":
        destination_symbol = template_to_use.route_symbols["destination"]
        connecting_symbol = template_to_use.route_symbols["connecting"]
        openjaw_symbol = template_to_use.route_symbols["openjaw"]

    organization_name = input("What is the name of the organization? ")
    default_currency = input("If there is no currency indicated, what should be used as the default? ")

    headers_after_reading, file_after_reading = read_historical_data_file(filename)

    if travel_mode == "flight":
        compare_headers(headers_after_reading, template_to_use.flight_headers, travel_mode)
        new_flight_file = clean_flight_data(file_after_reading, template_to_use.flight_headers, organization_name,
                                            destination_symbol, connecting_symbol, openjaw_symbol, default_currency)
        create_new_output_file(new_flight_file, travel_mode)
    elif travel_mode == "hotel":
        compare_headers(headers_after_reading, template_to_use.hotel_headers, travel_mode)
        new_hotel_file = clean_hotel_data(file_after_reading, template_to_use.hotel_headers, organization_name, default_currency)
        create_new_output_file(new_hotel_file, travel_mode)
