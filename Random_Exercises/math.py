"""
so running ((2+4)+3) will result 9
and we will do that with classes
in this case we will create a class that represents (2+4), let’s call it `left` (edited)
and then another one that represents (a+3)
and we need to implement a method called `calculate`

the only evaluation will happen when calling `calculate`
let’s keep it simple for now, support `+` and `-` only
"""


class Mathematical(object):
    pass


class Left(Mathematical):

    def __init__(self, equation):
        self.equation = equation

    def find_left(self):
        counter = 0
        left_side = ''
        while counter < len(self.equation):
            if self.equation[counter] == '(':
                left_side += equation[counter]


class Right(Mathematical):
    pass


print("Please enter a mathematical equation you would like to solve: ")
equation = input()







