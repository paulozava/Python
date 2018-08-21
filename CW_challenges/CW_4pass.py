def cnot(y, x):
    ''' docstring: return an integer representation of a cartesian map bidimencional y.x
        for exemple: y=0 and x=1 will return a cnot=1; y=1, x=0 will return a cnot=10
    '''
    return int(str(y) + str(x))

def four_pass(stations):
    for station in stations:
        coord = [divmod(stg, 10) for stg in station]
        x0, y0 = coord[0]
        coord = coord[1:]
        sliceble = [[], []]
        for x1, y1 in coord:
            xy = [cnot(y0, next_x) for next_x in range(x1 - x0)] + [cnot(next_y, x1) for next_y in range(y1 - y0 + 1)]
            yx = [cnot(next_y, x0) for next_y in range(y1 - y0)] + [cnot(y1, next_x) for next_x in range(x1 - x0 + 1)]
            left, right = sliceble[:int(len(sliceble))], sliceble[int(len(sliceble)):]
            if left:

            left = [[l.extend(xy)] for l in left]
            left = list(map(lambda z: z.append(xy), left))
            for l in right: l.extend(yx)
            sliceble = left + right
            x0, y0 = x1, y1



# example_tests = [
#         [1, 69, 95, 70],
#         [0, 49, 40, 99],
#         [37, 61, 92, 36],
#         [51, 24, 75, 57],
#         [92, 59, 88, 11]]
#
#
# station = [0,65,93,36]