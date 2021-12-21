"""Write a function named palindrome that takes a single string as its parameter. 
Your function should return True if the string is a palindrome, and False otherwise."""

def palindrome(string):
    rev_str = string[::-1]
    if string == rev_str:
        return True
    else:
        return False
    

palindrome("hellow")