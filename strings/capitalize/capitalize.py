def capitalize(words: str):
    words_list = words.split(" ")
    words_list_capitalized = list(map(lambda x: x.capitalize(), words_list))
    words_capitalized = " ".join(words_list_capitalized)
    print(words_capitalized)

capitalize("chris alan")