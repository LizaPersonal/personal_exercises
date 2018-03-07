# Program to illustrate a loop with condition at the top

# Try different numbers
n = 10

# Uncomment to get user input
# n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

# print the sum
print("The sum is", sum)