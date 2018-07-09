def reverse_it (iterator):
    new_iterator = []
    while iterator:
        new_iterator.append(iterator.pop())
    return iterator

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

def insertion_sort(iterator):
    # Stable
    # O(1) extra space
    # O(n2) comparisons and swaps
    # Adaptive: O(n) time when nearly sorted
    # Very low overhead
    iterator_length = len(iterator)
    for i in range(1, iterator_length):
        j = i
        while j > 0 and iterator[j] > iterator[j-1]:
            iterator[j], iterator[j - 1] = iterator[j - 1], iterator[j]
            j -= 1
    return reverse_it(iterator)