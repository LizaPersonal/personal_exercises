types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# The string binary and the string do_not are put inside the string y
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# The string x is put instide the print string
print("I said:",x)
# The string y is put inside the print string
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# This concatenates two strings
print(w + e)