"""Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, 
and False otherwise"""

def only_ints(x, y):
    if type(x) is int and type(y) is int:
        return True
    else:
        return False 


only_ints(1, 2)