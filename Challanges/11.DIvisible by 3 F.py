"""Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise."""

def div_3(num):
    if num % 3 == 0:
        return True
    else:
        return False

print(div_3(3))