def capitalize(words: str):
    words_list = words.split(" ")
    words_list_capitalized = list(map(lambda x: x.capitalize(), words_list))
    words_capitalized = " ".join(words_list_capitalized)
    return words_capitalized

print(capitalize("chris alan"))