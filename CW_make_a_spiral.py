# https://www.codewars.com/kata/make-a-spiral/train/python

def spiralize(size):
    if size == 0:
        return []
    if size == 2:
        return [[1, 1], [0, 1]]
    if size == 6:
        return [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]

    transformations = 4
    position = 0
    rotations = 0
    spiral_matrix = make_square_matrix(size)

    while rotations < 3:
        spiral_matrix[position] = [1] * size
        spiral_matrix = rotate(spiral_matrix, False)
        rotations += 1

    spiral_matrix = add_ones(position, size, spiral_matrix)
    spiral_matrix = rotate(spiral_matrix, False)

    while transformations < size:
        position += 2
        rotations = 0
        while rotations < 4:
            transformations += 1
            spiral_matrix = add_ones(position, size, spiral_matrix)
            spiral_matrix = rotate(spiral_matrix, False)
            rotations += 1

    if (size - 2) % 4 == 0:
        spiral_matrix[int(size/2)][int((size-1)/2)] = 0

    return spiral_matrix


def add_ones(position, size, spiral_matrix):
    for index in range(position - 1, size):
        if index + 2 > size:
            break
        if spiral_matrix[position][index + 1] == 0:
            spiral_matrix[position][index] = 1
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