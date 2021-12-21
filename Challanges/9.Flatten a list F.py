"""Write a function that takes a list of lists and flattens it into a one-dimensional list."""


def flatten(nested_list):
    flat_list = []
    for list in nested_list:
        for number in list:
            flat_list.append(number)
    return (flat_list)

flatten([[1, 2], [3, 4]])