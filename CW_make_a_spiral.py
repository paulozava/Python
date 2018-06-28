def spiralize(size):
    spital_matrix = make_spiral_matrix(size)
    return spital_matrix


def make_spiral_matrix(size):
    vertical = [0] * size
    horizontal = [vertical for i in range(size)]
    return horizontal