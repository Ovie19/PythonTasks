def get_sum_in_string(word):
    total = 0

    for character in word:
        if character in '123456789':
            total += int(character)
    return total