# https://www.codewars.com/kata/5904be220881cb68be00007d/train/python

#  	9.  Your size increments by one each time you reach the amounts below.

def fish(shoal, size = 1, protein_earned = 0):
    #  	1.  Your size starts at 1
    #  	2.  The shoal string will contain fish integers between 0-9
    #  	3.  0 = algae and wont help you feed.
    #  	4.  The fish integer represents the size of the fish (1-9).
    fishes = [int(fish) for fish in shoal if fish != '0']
    #  	5.  You can only eat fish the same size or less than yourself.
    edible_fishes = filter(lambda x: x <= size, fishes)
    #  	6.  You can eat the fish in any order you choose to maximize your size.
    #  	7.  You can and only eat each fish once.
    ate_protein = sum(edible_fishes)
    protein_earned += ate_protein
    #can grow?
    if protein_earned >= protein_to_grow(size):
        size += 1
    else:
        grow = False

    #  	8.  The bigger fish you eat, the faster you grow. A size 2 fish equals two size 1 fish, size 3 fish equals three size 1 fish, and so on.


def protein_to_grow(actual_size):
    sizes = [1,2,3,4,5,6,7,8,9]
    accumulate_sizes = filter(lambda x: x <= actual_size, sizes)
    protein_to_accumulate = sum([4*size for size in accumulate_sizes])
    return protein_to_accumulate