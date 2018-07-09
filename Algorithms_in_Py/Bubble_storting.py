
def bubble(x):
    last_element = x.pop()
    for n in range(len(x), 0, -1):
        if last_element <=


def proposed(a):
    n = len(a)
    for i in range(1, n):
        swapped = False
        for j in range(n, i + 1, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
