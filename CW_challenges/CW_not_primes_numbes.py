from itertools import product

def accumulate_products(max_turns, numbers=None):
    numbers = [str(digit) for digit in numbers]
    accumulators = []
    for repetition in range(1, max_turns + 1):
        accumulators.extend(product(numbers, repeat=repetition))
    accumulated_combinations = [int(''.join(item)) for item in accumulators]
    return accumulated_combinations


def not_primes(start, end, formers=(2, 3, 5, 7), limit=20000):
    turns = len(str(limit)) + 1
    possibilities = accumulate_products(turns, formers)
    possibilities = filter(lambda x: start<x<end, possibilities)
    founds=[]
    for possibility in possibilities:
        test = False
        if possibility % 2 != 0:
            test = all(possibility % i for i in range(3, possibility, 2))
        if not test:
            founds.append(possibility)
    return founds