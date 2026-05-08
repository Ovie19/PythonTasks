def swap_case(character):
    if character == 'A': return 'a'
    elif character == 'a': return 'A'
    elif character == 'B': return 'b'
    elif character == 'b': return 'B'
    elif character == 'C': return 'c'
    elif character == 'c': return 'C'
    elif character == 'D': return 'd'
    elif character == 'd': return 'D'
    elif character == 'E': return 'e'
    elif character == 'e': return 'E'
    elif character == 'F': return 'f'
    elif character == 'f': return 'F'
    elif character == 'G': return 'g'
    elif character == 'g': return 'G'
    elif character == 'H': return 'h'
    elif character == 'h': return 'H'
    elif character == 'I': return 'i'
    elif character == 'i': return 'I'
    elif character == 'J': return 'j'
    elif character == 'j': return 'J'
    elif character == 'K': return 'k'
    elif character == 'k': return 'K'
    elif character == 'L': return 'l'
    elif character == 'l': return 'L'
    elif character == 'M': return 'm'
    elif character == 'm': return 'M'
    elif character == 'N': return 'n'
    elif character == 'n': return 'N'
    elif character == 'O': return 'o'
    elif character == 'o': return 'O'
    elif character == 'P': return 'p'
    elif character == 'p': return 'P'
    elif character == 'Q': return 'q'
    elif character == 'q': return 'Q'
    elif character == 'R': return 'r'
    elif character == 'r': return 'R'
    elif character == 'S': return 's'
    elif character == 's': return 'S'
    elif character == 'T': return 't'
    elif character == 't': return 'T'
    elif character == 'U': return 'u'
    elif character == 'u': return 'U'
    elif character == 'V': return 'v'
    elif character == 'v': return 'V'
    elif character == 'W': return 'w'
    elif character == 'w': return 'W'
    elif character == 'X': return 'x'
    elif character == 'x': return 'X'
    elif character == 'Y': return 'y'
    elif character == 'y': return 'Y'
    elif character == 'Z': return 'z'
    elif character == 'z': return 'Z'
    else: return character

def toggle_case(word):
    toggle_word = ""

#    for character in word:
#        if character == character.lower():
#            toggle_word += character.upper()
#        else:
#            toggle_word += character.lower()

    for character in word:
        toggle_word += swap_case(character)

    return toggle_word



"""
a - 97
A - 65
z - 122
Z - 90
"""