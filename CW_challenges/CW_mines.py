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


for yindex, line in enumerate(mapline):
    if '0' in line:
        for xindex, item in enumerate(line):
            if item == '0':
                if xindex > 0:
                    mapline[yindex][xindex - 1] = open(xindex-1, yindex)
                if xindex < len(line):
                    mapline[yindex][xindex + 1] = open(xindex+1, yindex)
                if yindex > 0:
                    mapline[yindex - 1][xindex] = open(xindex, yindex-1)
                if yindex < len(mapline):
                    mapline[yindex + 1][xindex] = open(xindex, yindex+1)