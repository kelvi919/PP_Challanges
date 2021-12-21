"""Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, 
both inclusive, and return it."""

import random
def random_number():
    rand_num = random.randint(0, 101)
    return (rand_num)

random_number()
