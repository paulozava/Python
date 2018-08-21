# https://www.codewars.com/kata/four-pass-transport/train/python

def cnot(y, x):
    ''' docstring: return an integer representation of a cartesian map bidimencional y.x
        for exemple: y=0 and x=1 will return a cnot=1; y=1, x=0 will return a cnot=10
    '''
    return int(str(y) + str(x))

def four_pass(stations):
    final = possibles_paths(stations)
    for item in sorted(final):
        if len(item) == len(set(item)):
            return item
    return []


def possibles_paths(stations):
    coord = [divmod(stg, 10) for stg in stations]
    y0, x0 = coord[0]
    coord = coord[1:]
    final = []
    for y1, x1 in coord:
        if x0 > x1:
            xdif = [x0, x1, -1]
        else:
            xdif = [x0, x1, 1]
        if y0 > y1:
            ydif = [y0, y1, -1]
        else:
            ydif = [y0, y1, 1]

        xy = [cnot(y0, next_x) for next_x in range(*xdif)]
        yx = [cnot(next_y, x0) for next_y in range(*ydif)]

        xdif[1] += xdif[2]
        ydif[1] += ydif[2]

        xy += [cnot(next_y, x1) for next_y in range(*ydif)]
        yx += [cnot(y1, next_x) for next_x in range(*xdif)]

        if final:
            left, right, parcial = [], [], []
            for item in final:
                left = item + xy[1:]
                right = item + yx[1:]
                parcial.append(left)
                parcial.append(right)
            final = parcial
        else:
            final.append(xy)
            final.append(yx)
        y0, x0 = y1, x1
    return final


# if __name__ == '__main__':
#     example_tests = [
#         [1, 69, 95, 70],
#         [0, 49, 40, 99],
#         [37, 61, 92, 36],
#         [51, 24, 75, 57],
#         [92, 59, 88, 11]]
#     for s in example_tests:
#         x = four_pass(s)
#         print(x)
#         print(len(x))
