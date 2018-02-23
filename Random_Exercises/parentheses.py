
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
    equal = validate_equal_parentheses(user_input)
    mathematical = validate_math_logic(user_input)
    return(equal, mathematical)

def validate_equal_parentheses(user_input):
    counter = 0
    open = 0
    close = 0

    if user_input == None:
        raise GeneralError()
    input_length = len(user_input)

    while counter < input_length:
        if user_input[counter] in ("("):
            open += 1
            counter += 1
        elif user_input[counter] in (")"):
            close += 1
            counter += 1
        else:
            raise NotValidString()

    result = open == close
    if result:
        return result
    else:
        raise NotEqualOpenCloseParentheses()


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
        raise NotMathematicalLogic() #What if the result isn't true because it is invalid?


if __name__ == '__main__':
    user_input = get_user_input()

    # valid = validate_equal_parentheses(user_input)
    #
    # while not valid:
    #     user_input = get_user_input()
    #
    #     valid = validate_equal_parentheses(user_input)




    # if we need to reset:
    #     user_input = get_user_input()

    try:
        input = validate_expression(user_input)
        if input.equal:
            print("This string has equal open and close parentheses.\nIt passes this test.\n")
        if input.mathematical:
            print("This string has accurate mathematical logic.\nIt passes this test.\n")
    except GeneralError:
        print("error")
    except NotEqualOpenCloseParentheses:
        print("\nThis string does NOT have equal open and close parentheses.\nIt does not pass this test.\n")
        print("It cannot follow mathematical logic.\n")
    except NotMathematicalLogic:
        print("This string does NOT follow mathematical logic.\nIt does not pass this test.\n")
    except NotValidString:
        print("Not a valid string")





