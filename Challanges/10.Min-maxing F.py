"""Your function should compute and return the difference between the largest and smallest number in the list."""

def largest_difference(my_list):
    max_num = max(my_list)
    min_num = min(my_list)
    diff = max_num - min_num
    return (diff)

largest_difference([1, 2, 3])