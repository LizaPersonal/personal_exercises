from .ex48_convert import convert_number


dictionary = {"north": "direction", "south": "direction", "east": "direction", "go": "verb", "kill": "verb",
              "eat": "verb", "the": "stop", "in": "stop", "of": "stop", "bear": "noun", "princess": "noun"}


def scan(user_input):
    sentence = []
    words = user_input.split()
    for word in words:
        int_word = convert_number(word)
        if word.lower() in dictionary:
            sentence.append((dictionary[word], word))
        elif int_word is not None:
            sentence.append(('number', int_word))
        else:
            sentence.append(('error', word))
    return sentence


# if __name__ == '__main__':
#     final = scan("123")
#     print(final)
