def left_riemman(function, retangles, start_point, end_point):
    delta = (end_point - start_point) / retangles
    area = 0
    for i in range(retangles):
        area += function(start_point) * delta
        start_point += delta
    return area

def right_riemman(function, retangles, start_point, end_point):
    delta = (end_point - start_point) / retangles
    area = 0
    for i in range(retangles):
        start_point += delta
        area += function(start_point) * delta
    return area

def midlle_riemman(function, retangles, start_point, end_point):
    delta = (end_point - start_point) / retangles
    start_point += delta / 2
    area = 0
    for i in range(retangles):
        area += function(start_point) * delta
        start_point += delta
    return area

def elements_left_riemman(function, retangles, start_point, end_point):
    delta = (end_point - start_point) / retangles
    area = []
    for i in range(retangles):
        left_point = function(start_point)
        area.append(left_point)
        start_point += delta
    return area

def elements_right_riemman(function, retangles, start_point, end_point):
    delta = (end_point - start_point) / retangles
    area = []
    for i in range(retangles):
        start_point += delta
        right_point = function(start_point)
        area.append(right_point)
    return area

def riemann_trapezoidal(function, retangles, start_point, end_point):
    delta = (end_point - start_point) / retangles
    left_points = elements_left_riemman(function, retangles, start_point, end_point)
    right_points = elements_right_riemman(function, retangles, start_point, end_point)
    area = 0
    for right_point, left_point in zip(right_points, left_points):
        area += ((right_point + left_point)/2)*delta
    return area