"""Define a function named up_down that takes a single number as its parameter. 
Your function return a tuple containing two numbers; the first should be one lower than the parameter, 
and the second should be one higher."""

def up_down(num):
    up_num = num + 1 
    down_num = num - 1
    tuple = (down_num, up_num)
    return tuple
up_down(6)