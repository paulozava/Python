def reverse_it (iterator):
    new_iterator = []
    while iterator:
        new_iterator.append(iterator.pop())
    iterator.append(new_iterator)
    return iterator

def bubble(iterator=None):
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

def insertion_sort(iterator=None):
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

def selection (iterator=None):
    # Not stable
    # O(1) extra space
    # Θ(n2) comparisons
    # Θ(n) swaps
    # Not adaptive
    iterator_length = len(iterator)
    for i in range(iterator_length):
        k = i
        for j in range(i+1, iterator_length):
            if iterator[j] < iterator[k]:
                iterator[j], iterator[k] = iterator[k], iterator[j]
    return iterator