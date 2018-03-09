''' Python program to chuffle a deck of cards using the module random and draw 5 cards '''

# import modules
import itertools
import random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade\'s', 'Heart\'s', 'Diamond\'s', 'Club\'s']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
