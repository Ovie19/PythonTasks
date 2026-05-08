def get_vowel_count(word):
    vowels_found = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for character in word.lower():
        if character in vowels and character not in vowels_found:
            vowels_found.append(character)

    return len(vowels_found)

word = "Pineapple"
print(f"The number of vowels in {word} is {get_vowel_count(word)}")
word = "Fry"
print(f"The number of vowels in {word} is {get_vowel_count(word)}")