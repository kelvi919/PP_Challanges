"""Define a function named count that takes a single parameter. 
The parameter is a string. 
The string will contain a single word divided into syllables by hyphens, 
such as these:'met-a-phor', 'ter-min-a-tor' 
Your function should count the number of syllables and return it.
"""

def count(string):
    hyphens = 1 
    
    for letter in string:
        if letter == "-":
            hyphens += 1
    
    return (hyphens)

count("ho-tel")