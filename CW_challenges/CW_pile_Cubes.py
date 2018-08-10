def find_nb(m):
    n = 0
    for i in range(m):
        m -= i ** 3
        n += 1
        if m == 0:
            print('inteiro')
            break
        elif m < 0:
            return -1