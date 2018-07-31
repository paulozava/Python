def left_riemman(function, n, a, b):
    delta = (b - a) / n
    area = 0
    for i in range(n):
        area += function(a) * delta
        a += delta
    return area

def right_riemman(function, n, a, b):
    delta = (b - a) / n
    area = 0
    for i in range(n):
        a += delta
        area += function(a) * delta
    return area

def midlle_riemman(function, n, a, b):
    delta = (b - a) / n
    a += delta/2
    area = 0
    for i in range(n):
        area += function(a) * delta
        a += delta
    return area

def elements_left_riemman(function, n, a, b):
    delta = (b - a) / n
    area = []
    for i in range(n):
        left_point = function(a)
        area.append(left_point)
        a += delta
    return area

def elements_right_riemman(function, n, a, b):
    delta = (b - a) / n
    area = []
    for i in range(n):
        a += delta
        right_point = function(a)
        area.append(right_point)
    return area

def riemann_trapezoidal(function, n, a, b):
    delta = (b - a) / n
    left = elements_left_riemman(function, n, a, b)
    right = elements_right_riemman(function, n, a, b)
    area = 0
    for r, l in zip(right, left):
        area += ((r + l)/2)*delta
    return area