# Python Program to find the L.C.M. of two input number


# define a function
def lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if(greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


# define gcd function
def gcd(x, y):
    """This function implements the Euclidian algorithm
    to find G.C.D. of two number"""

    while y:
        x, y = y, x % y

    return x


# define the new lcm function
def new_lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""

    lcm = (x * y) // gcd(x, y)
    return lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1, "and", num2, "is", lcm(num1, num2))
print("The L.C.M. of", num1, "and", num2, "is", new_lcm(num1, num2))