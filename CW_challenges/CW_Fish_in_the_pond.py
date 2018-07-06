def fish(shoal, size = 1, protein_earned = 0):
    fishes = [int(fish) for fish in shoal if fish != '0']
    grow = True
    while grow:
        edible_fishes = filter(lambda x: x <= size, fishes)
        ate_protein = sum(edible_fishes)
        protein_earned += ate_protein
        if protein_earned >= protein_to_grow(size):
            size += 1
            fishes = [fish for fish in fishes if fish not in edible_fishes]
        else:
            grow = False
    return size

def protein_to_grow(actual_size):
    sizes = [1,2,3,4,5,6,7,8,9]
    accumulate_sizes = filter(lambda x: x <= actual_size, sizes)
    protein_to_accumulate = sum([4*size for size in accumulate_sizes])
    return protein_to_accumulate