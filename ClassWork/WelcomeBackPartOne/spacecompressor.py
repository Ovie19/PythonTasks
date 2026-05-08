def compress_space(word):
    compress_word = ""

    for character in word:
        if character != " ": compress_word += character
        else: compress_word += "-"

    return compress_word