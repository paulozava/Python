# https://www.codewars.com/kata/make-a-spiral/train/python

def spiralize(size):
    position = 0
    rotations = 0
    spiral_matrix = make_square_matrix(size)

    spiral_matrix[position] = [1] * size
    spiral_matrix = rotate(spiral_matrix, False)
    spiral_matrix[position] = [1] * size
    spiral_matrix = rotate(spiral_matrix, False)
    spiral_matrix[position] = [1] * size
    spiral_matrix = rotate(spiral_matrix, False)

    while rotations < 4:


    for index in range(position-1, size):
        if index + 2 > size:
            break
        if spiral_matrix[position][index + 1] == 0:
            spiral_matrix[position][index] = 1

    position += 2
    spiral_matrix = rotate(spiral_matrix, False)

    return spiral_matrix


def make_square_matrix(size):
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