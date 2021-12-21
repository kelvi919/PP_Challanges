"""Write a function named capital_indexes. 
The function takes a single parameter, which is a string. 
Your function should return a list of all the indexes in the string that have capital letters.
"""


def capital_indexes(string):
    result = []
    for index, element in enumerate(string):
        if element == element.capitalize():
            result.append(index)
   
    return(result)


capital_indexes("HeLlO")
