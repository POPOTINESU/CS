l_1 = ["MOn", "Tue"]


def change_words(words, func):
    for word in words:
        print(func(word))


change_words(l_1, lambda word: word.capitalize())
change_words(l_1, lambda word: word.lower())
