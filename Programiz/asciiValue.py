def character_to_ascii():
    """program to find the ASCII value of the given character"""
    c = input("Enter a character: ")
    print("The ASCII value of '" + c+"' is", ord(c))


def ascii_to_character():
    """program to find the ASCII value of the given character"""
    c = int(input("Enter a ASCII value: "))
    print("The character for ASCII value '{}' is {}".format(c, chr(c)))


if __name__ == '__main__':
    character_to_ascii()
    ascii_to_character()