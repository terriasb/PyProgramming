# Giraffe language
# vowels become "g"
# dog -> dgg
# cat -> cgt
'''
This is a block comment
i
'''


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": # checks if any letter(vowels) in the string is in the phrase
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
# essentially rebuilding the phrase letter by letter and replacing vowels with g
# Challenge make the program case-sensitive


print(translate(input("Enter a phrase: ")))