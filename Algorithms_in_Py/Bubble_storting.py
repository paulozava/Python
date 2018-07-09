def bubble(iterator, reverse=False):
    iterator_length = len(iterator)
    for i in range(0, iterator_length):
        swapped = False
        for j in range(iterator_length -1, i , -1):
            if iterator[j] < iterator[j - 1]:
                iterator[j], iterator[j - 1] = iterator[j - 1], iterator[j]
                swapped = True
        if not swapped:
            break
    return iterator
