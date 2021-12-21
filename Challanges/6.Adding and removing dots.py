"""Write a function named add_dots that takes a string and adds "." in between each letter.
For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
For example, calling remove_dots("t.e.s.t") should return "test"."""

def add_dots(string):
    letter_list = [] 
    for letter in string:
        letter_list += letter, 

    joined_list = ".".join(letter_list)
    return joined_list


def remove_dots(string):
    letter_list = [] 
    for letter in string:
        if letter != ".":
            letter_list.append(letter)
    
    joined_list = "".join(letter_list)
    return (joined_list)



remove_dots(add_dots("hellow"))