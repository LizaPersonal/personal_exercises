
class GeneralError(Exception):
    pass


class NotMathematicalLogic(Exception):
    pass


class NotEqualOpenCloseParentheses(Exception):
    pass


class NotValidString(Exception):
    pass


def get_user_input():
    user_input = str(input("Please provide a string of parentheses: "))
    return user_input


def validate_expression(user_input):
    if user_input == None:
        raise GeneralError()
    validate_equal_parentheses(user_input)
    validate_math_logic(user_input)


def validate_equal_parentheses(user_input):
    if user_input == None:
        raise GeneralError()
    input_length = len(user_input)
    open_parentheses = user_input.count("(")
    close_parentheses = user_input.count(")")
    if input_length == open_parentheses + close_parentheses:
        if open_parentheses == close_parentheses:
            return True
        else:
            raise NotEqualOpenCloseParentheses()
    else:
        raise NotValidString()


def validate_math_logic(user_input):
    counter = 0
    pair = 0
    if user_input == None:
        raise GeneralError()
    input_length = len(user_input)

    while counter < input_length:
        if user_input.startswith("("):
            pair += 1
            counter += 1
            while (counter < input_length) and (pair > 0):
                if user_input[counter] in "(":
                    pair += 1
                    counter += 1
                elif user_input[counter] in ")":
                    pair -= 1
                    counter += 1
                else:
                    raise NotValidString()
        elif user_input.startswith(")"):
            raise NotMathematicalLogic()
        else:
            counter = input_length
            pair -= 1

    result = pair == 0
    if result:
        return result
    else:
        raise NotMathematicalLogic()


def get_user_input_and_validate():
    should_retry = False

    user_input = get_user_input()
    try:
        validate_expression(user_input)
        print("success!!!")
    except GeneralError:
        print("error")
    except NotEqualOpenCloseParentheses:
        print("\nThis string does NOT have equal open and close parentheses.\nIt does not pass this test.\n")
        print("It cannot follow mathematical logic.\n")
    except NotMathematicalLogic:
        print("This string does NOT follow mathematical logic.\nIt does not pass this test.\n")
    except NotValidString:
        print("Not a valid string")
        should_retry = True

    return should_retry


if __name__ == '__main__':
    retry = get_user_input_and_validate()
    while retry:
        retry = get_user_input_and_validate()






