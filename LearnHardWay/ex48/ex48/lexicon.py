
dictionary = {"north": "direction", "south": "direction", "east": "direction", "go": "verb", "kill": "verb",
              "eat": "verb", "the": "stop", "in": "stop", "of": "stop", "bear": "noun", "princess": "noun"}


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(user_input):
    sentence = []
    words = user_input.split()
    for word in words:
        if word.lower() in dictionary:
            next_word = (dictionary[word], word)
            sentence.append(next_word)
        elif convert_number(word) != None:
            number_not_word = ('number', int(word))
            sentence.append(number_not_word)
        else:
            next_word = ('error', word)
            sentence.append(next_word)
    return sentence


# if __name__ == '__main__':
#     final = scan("123")
#     print(final)
