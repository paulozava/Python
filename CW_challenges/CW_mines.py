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


def solve_mine(map, n):
    pass

map = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip()

mapline = [line.split(' ') for line in map.split('\n')]
map_transpose = rotate(mapline)

for line in mapline:
    for item in line:
        if '0' == item:

