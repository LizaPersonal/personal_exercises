import string


def update_employee_name(read_file, flight_headers_in_file):
    """ Identify which column represents the employee name.
        Identify if the column contains 'first last' or 'last, first'
        For each row correct the casing for the employee name.
        Update the file with the name. """

    header_to_look_for = flight_headers_in_file["employee_name"]
    format_in_file = _review_name_format(read_file, header_to_look_for)

    for row in read_file:
        name_in_file = row[header_to_look_for]
        formatted_name = _update_name_format(name_in_file, format_in_file)
        case_corrected_name = _set_name_to_correct_case(formatted_name)
        row[header_to_look_for] = case_corrected_name
    return read_file


def _review_name_format(read_file, employee_name_header):
    """ Take in a name and identify if it is 'first last' or 'last, first'. """

    count_slash = 0
    count_comma = 0
    total_count = 0

    for row in read_file:
        total_count += 1
        if "/" in row[employee_name_header]:
            count_slash += 1
        elif "," in row[employee_name_header]:
            count_comma += 1

    if count_slash/total_count > .75:
        return '/'
    elif count_comma/total_count > .75:
        return ','
    else:
        return ' '


def _update_name_format(name_in_file, starting_format):
    """ Take the name and correct the format based on the starting format. """

    whole_name = ""

    if starting_format != '':
        parsed_name = name_in_file.split(starting_format)
        for name in range(len(parsed_name)):
            name += 1
            if name < len(parsed_name):
                whole_name += parsed_name[name] + " "
        whole_name += parsed_name[0]
    else:
        whole_name = name_in_file

    return whole_name


def _set_name_to_correct_case(name_in_file):
    """ Take the name and correct the casing of the letters. """

    corrected_name = string.capwords(name_in_file, ' ')
    return corrected_name
