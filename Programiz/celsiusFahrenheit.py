def celsius2fahrenheit():
    celsius = float(input("Enter value in celsius: "))

    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius, fahrenheit))


def fahrenheit2celsius():
    fahrenheit = float(input("Enter value in fahrenheit: "))

    celsius = (fahrenheit - 32) / 1.8
    print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheit, celsius))


if __name__ == '__main__':
    celsius2fahrenheit()
    fahrenheit2celsius()