formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4,))
print(formatter.format("one", "two", "three", "four"))
# The answer to the first question for this exercise is incorrectly answered
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))