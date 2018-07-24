
def update_room_type(read_file, headers_in_file):

    header_to_look_for = headers_in_file["room_type"]
    for row in read_file:
        if row.get(header_to_look_for) is not None:
            room_type_in_file = row[header_to_look_for]
            formatted_room_type = _remove_unnecessary_characters(room_type_in_file)
            row["room_type"] = formatted_room_type
    return read_file


def _remove_unnecessary_characters(text_in_file):
    remove_less_than = text_in_file.replace("<", "")
    remove_greater_than = remove_less_than.replace(">", "")
    remove_space = remove_greater_than.strip()
    return remove_space
