from math import ceil

def get_candy_position(number_candies, row, col, find_candy):
    if find_candy > number_candies: return [-1,-1,-1]
    box_spot = row * col
    box = ceil(find_candy/box_spot)
    row_c = row - ceil((find_candy % box_spot) / col)
        if row_c == row: row_c = 0
    col_c = col - (find_candy % col)
    resp = [box, row_c, col_c]
    return resp