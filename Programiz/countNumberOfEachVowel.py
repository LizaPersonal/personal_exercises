# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# change this value for a different result
ip_str = 'Hello, have you tried our tutorial section yet?'

# un commet to take input from the user
# ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1

print(count)

# Program to count the number of each vowel in a string using dictionary and list comprehension

count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)