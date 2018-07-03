def boxBlur(image):
    x_axis, y_axis = len(image[0]), len(image)
    box_blur = []
    for y in range(y_axis -2):
        line = []
        for x in range(x_axis-2):
            parcial = []
            parcial.extend(image[y][x:x+3])
            parcial.extend(image[y+1][x:x+3])
            parcial.extend(image[y+2][x:x+3])
            pix_avg = int(sum(parcial) / len(parcial))
            line.append(pix_avg)
        box_blur.append(line)
    return box_blur