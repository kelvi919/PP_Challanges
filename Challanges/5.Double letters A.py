"""The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
For example, the string "hello" has l twice in a row, 
while the string "nono" does not have two identical letters in a row."""

def double_letters(string):
    last_letter = ""

    # store letter into last_letter and check if next letter is equal to last_letter, if so return True
    for index, letter in enumerate(string):
        print(string.index(letter))

        if string.index(letter) == index:
            print("double")

    print(len(string))
    print(string)

double_letters("aab")

