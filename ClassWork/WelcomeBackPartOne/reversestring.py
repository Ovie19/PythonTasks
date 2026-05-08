def get_reverse_string(word):
    reverse = ""
    for character in word:
        reverse = character + reverse

    return reverse

word = "eggroll"
print(word)
print(get_reverse_string(word))