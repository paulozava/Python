# https://www.codewars.com/kata/four-pass-transport/train/python

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
        sliceble = []
        for x1, y1 in coord:
            if x0 > x1: xdif = [x0, x1, -1]
            else: xdif = [x0, x1, 1]
            if y0 > y1: ydif = [y0, y1, -1]
            else: ydif = [y0, y1, 1]

            xy = [cnot(y0, next_x) for next_x in range(*xdif)]
            yx = [cnot(next_y, x0) for next_y in range(*ydif)]

            xdif[1]+=xdif[2]
            ydif[1]+=ydif[2]

            xy += [cnot(next_y, x1) for next_y in range(*ydif)]
            yx += [cnot(y1, next_x) for next_x in range(*xdif)]

            if sliceble:
                left, right = list(sliceble), list(sliceble)
                for index in range(len(sliceble)):
                    left[index].append(xy)
                    right[index].append(yx)
                sliceble = [left, right]
            else:
                sliceble.append(xy)
                sliceble.append(yx)
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