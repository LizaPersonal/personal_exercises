
def create_list(user_max, user_increment):
    i = 0
    numbers = []

    while i < (user_max + 1):
        print(f"At the top i is {i}")
        numbers.append(i)

        i += user_increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers


if __name__ == '__main__':
    user_max = int(input("What is the max number you would like to add? "))
    user_increment = int(input("How far apart should the numbers be spaced? "))
    numbers = create_list(user_max, user_increment)
    print("The numbers: ")

    for num in numbers:
        print(num)
