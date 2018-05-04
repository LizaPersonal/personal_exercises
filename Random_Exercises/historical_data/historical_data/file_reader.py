import csv
# from ..tmc_templates import default
import check_airline_vendors
# import check_domestic_vs_international
# import check_connecting_vs_nonstop
# from ..app import upload_historical_data


def read_historical_data_file(file):
    with open(file, "r", newline='') as historical_data_file:
        # file_to_read = (line.decode('utf8', 'ignore') for line in historical_data_file.read().splitlines())
        read_file = []
        reader = csv.DictReader(historical_data_file)
        headers = reader.fieldnames
        for row in reader:
            read_file.append(row)
    return headers, read_file


def print_historical_csv(read_file):
    for row in read_file:
        print(row)


def validate_airline(read_file):
    for row in read_file:
        header_to_look_for = 'Vendor *'
        airline_in_file = row[header_to_look_for]
        # vendor_code = check_airline_vendors.validate_airline_vendor({header_to_look_for: airline_in_file})
        vendor_code = check_airline_vendors.validate_airline_vendor((airline_in_file, ))
        row[header_to_look_for] = vendor_code[0]
        # print(row)
    return read_file


def create_new_output_file(updated_file, fields):
    writer = csv.DictWriter(open('/tmp/output.csv', "w+"), fieldnames=fields)
    writer.writeheader()
    writer.writerows(updated_file)


# filename, tmc, travel_mode, organization_name = upload_historical_data()

filename = input("What file would you like to read? ")

# tmc = input("Which TMC is the file from? ")
#
# travel_mode = input("What type of travel are you looking to upload? ")
#
# organization_name = input("What is the name of the organization? ")

headers_after_reading, file_after_reading = read_historical_data_file(filename)
# print_historical_csv(headers_after_reading)
updated_airlines = validate_airline(file_after_reading)
create_new_output_file(updated_airlines, headers_after_reading)

