def minesweeper(matrix):
    x_axis, y_axis = len(matrix[0]), len(matrix)
    new_matrix = []
    for y in range(y_axis):
        line = []
        for x in range(x_axis):
            neighbour = []
            if x > 0:
                neighbour.extend(matrix[y][x-1])
                if y > 0:
                   neighbour.extend(matrix[y - 1][x - 1])
                if y < y_axis - 1:
                    neighbour.extend(matrix[y + 1][x - 1])
            if x < x_axis -1:
                neighbour.extend(matrix[y][x + 1])
                if y > 0:
                    neighbour.extend(matrix[y - 1][x + 1])
                if y < y_axis - 1:
                    neighbour.extend(matrix[y + 1][x + 1])
            if y > 0:
                neighbour.extend(matrix[y-1][x])
            if y < y_axis -1:
                neighbour.extend(matrix[y+1][x])
            mines = neighbour.count(True)
            line.append(mines)
        new_matrix.append(line)
    return new_matrix