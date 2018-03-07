def kilometers2miles():
    # Take kilometers from the user
    kilometers = float(input("Enter value in kilometers: "))

    # conversion factor
    conv_fac = 0.621371

    # calculate miles
    miles = kilometers * conv_fac
    print('%0.3f kilometers is equal to %0.3f miles' %(kilometers, miles))


def miles2kilometers():
    # Take miles from the user
    miles = float(input("Enter value in miles: "))

    # conversion factor
    conv_fac = 1.60934

    # calculate kilometers
    kilometers = miles * conv_fac
    print('%0.3f miles is equal to %0.3f kilometers' %(miles, kilometers))


if __name__ == '__main__':
    kilometers2miles()
    miles2kilometers()