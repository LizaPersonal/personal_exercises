import csv
import check_airline_vendors
from ..tmc_templates import default
# import check_domestic_vs_international
# import check_connecting_vs_nonstop
# from ..app import upload_historical_data


def read_historical_data_file(file):
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
        default_tmc_flight_headers = default.DefaultFlights()
        return default_tmc_flight_headers
    else:
        print("That is not a valid TMC at this time.")
        return None


def validate_airline(read_file, header_to_look_for):
    for row in read_file:
        header_to_look_for = 'Vendor *'
        airline_in_file = row[header_to_look_for]
        vendor_code = check_airline_vendors.validate_airline_vendor((airline_in_file, ))
        row[header_to_look_for] = vendor_code[0]
    return read_file


def create_new_output_file(updated_file, fields):
    writer = csv.DictWriter(open('/tmp/output.csv', "w+"), fieldnames=fields)
    writer.writeheader()
    writer.writerows(updated_file)


if __name__== "__main__":

    filename = input("What file would you like to read? ")
    flight_headers = validate_tmc()


    # travel_mode = input("What type of travel are you looking to upload? ")
    #
    # organization_name = input("What is the name of the organization? ")

    headers_after_reading, file_after_reading = read_historical_data_file(filename)
    updated_airlines = validate_airline(file_after_reading)
    create_new_output_file(updated_airlines, headers_after_reading)

