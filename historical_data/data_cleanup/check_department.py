from data_cleanup.check_employee_name import set_name_to_correct_case


def update_department(read_file, headers_in_file):

    header_to_look_for = headers_in_file["department"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            department_in_file = row[header_to_look_for]
            formatted_department = set_name_to_correct_case(department_in_file)
            row["department"] = formatted_department
    return read_file
