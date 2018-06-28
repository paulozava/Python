# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

def snail(array):
    snail_array = []

    while len(array) > 0:
        snail_array.extend(array.pop(0))

        length_array = len(array)
        for i in range(length_array):
            adder = array[i].pop(-1)
            snail_array.append(adder)

        if length_array > 0:
            array[-1].reverse()
            snail_array.extend(array.pop(-1))

        length_array = len(array)
        for i in range(length_array -1, -1, -1):
            adder = array[i].pop(0)
            snail_array.append(adder)

    return snail_array