def convertToBinary(n):
    """Function to print binary number
    for the input decimal using recursion"""
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end='')


dec = int(input("Enter a number to convert: "))

convertToBinary(dec)