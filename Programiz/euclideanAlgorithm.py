def computeHCF(x, y):

    # This function implements the Euclidian algorithm to find H.c.F. of two numbers
    while y:
        x, y = y, x % y

    return x


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))
