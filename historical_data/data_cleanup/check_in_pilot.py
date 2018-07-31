from data_cleanup.check_employee_name import set_name_to_correct_case


def update_in_pilot(read_file, headers_in_file):

    header_to_look_for = headers_in_file["in_pilot"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            pilot_in_file = row[header_to_look_for]
            formatted_pilot = _standardize_pilot_field(pilot_in_file)
            row["in_pilot"] = formatted_pilot
    return read_file


def _standardize_pilot_field(pilot_in_file):
    formatted_pilot = set_name_to_correct_case(pilot_in_file)
    if formatted_pilot not in ["Yes", "No"]:
        if formatted_pilot == "":
            return formatted_pilot
        elif formatted_pilot == 1:
            return "Yes"
        elif formatted_pilot == 0:
            return "No"
        else:
            pilot_indicator = input(formatted_pilot+" is not a Yes or No. Which should it indicate for this client?")
            if pilot_indicator in ["Yes", "No"]:
                return pilot_indicator
            else:
                _standardize_pilot_field(pilot_in_file)
    else:
        return formatted_pilot
