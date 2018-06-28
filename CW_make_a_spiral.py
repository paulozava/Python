# https://www.codewars.com/kata/make-a-spiral/train/python

def spiralize(size):
    snake_max_path = size
    spital_matrix = make_spiral_matrix(size)
    for path in range(snake_max_path):

    spital_matrix = rotate(spital_matrix)
    return spital_matrix


def make_spiral_matrix(size):
    matrix = [[0] * size for i in range(size)]
    return matrix

def rotate (matrix, clockwise=True):
    new_matrix = []
    size = len(matrix)
    for horizontal in range(size):
        new_line = []
        for vertical in range(size):
            element = matrix[vertical][horizontal]
            new_line.append(element)
        if clockwise:
            new_line.reverse()
        new_matrix.append(new_line)
    if not clockwise:
        new_matrix.reverse()
    return new_matrix

def test (matrix, size):
    matrix[0] = [1 for i in range(size)]
    matrix[-1] = [1 for i in range(size)]
