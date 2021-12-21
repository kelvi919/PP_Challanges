"""Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.
"""


def mid(string):
   
    if len(string) % 2 != 0:
        string_nr = len(string) // 2
        return(string[string_nr])
    else:
        return("")

mid("abss")
