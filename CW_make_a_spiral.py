# https://www.codewars.com/kata/make-a-spiral/train/python

def spiralize(size):
    transformations = 4
    position = 0
    rotations = 0
    spiral_matrix = make_square_matrix(size)

    while rotations < 3:
        spiral_matrix[position] = [1] * size
        spiral_matrix = rotate(spiral_matrix, False)
        rotations += 1

    while transformations < size:
        position += 2
        rotations = 0
        while rotations < 4:
            transformations += 1
            for index in range(position-1, size):
                if index + 2 > size:
                    break
                if spiral_matrix[position][index + 1] == 0:
                    spiral_matrix[position][index] = 1
            spiral_matrix = rotate(spiral_matrix, False)
            rotations += 1

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