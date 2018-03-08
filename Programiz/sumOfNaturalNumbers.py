# Python program to find the sum of natural numbers up to n where n is provided by user
def loop_2_find_sum():
    num = int(input("Enter a number: "))
    if num < 0:
        num = int(input("Enter a positive number"))
    else:
        sum = 0
        # use while loop to iterate until zero
        while num > 0:
            sum += num
            num -= 1
        print("The sum is", sum)


def equation_2_find_sum():
    num = int(input("Enter a number: "))
    if num < 0:
        num = int(input("Enter a positive number"))
    else:
        sum = num * (num + 1) / 2
        print("The sum is", sum)


if __name__ == '__main__':
    loop_2_find_sum()
    equation_2_find_sum()