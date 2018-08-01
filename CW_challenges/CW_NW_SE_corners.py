def box(coords):
    nw, se = [], []
    longest = lambda x,y: (x**2) + (y**2)
    max_nw, max_se = 0,0
    for lat, long in map(tuple, coords):
        if lat > 0 and long < 0:
            distance = longest(lat, long)
            if max_nw < distance:
                nw = [lat, long]
                max_nw = distance
        elif lat < 0 and long > 0:
            distance = longest(lat, long)
            if max_se < distance:
                se = [lat, long]
                max_se = distance
    return {'nw': nw, 'se': se}

b = [[ -32, -143 ], [ 68, 165 ], [ -70, 165 ], [ -32, -130 ], [ -14, 118 ], [ -48, -136 ], [ 15, 29 ], [ -70, 50 ], [ -14, -179 ], [ 35, -72 ], [ 8, -19], [ 68, -179 ]]

box(b)

{ "nw": [ 68, -179 ], "se": [ -70, 165 ] }