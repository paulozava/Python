def how_to_find_them(biangle):
    if 'c' in biangle:
        hip = biangle['c']
        if 'a' in biangle:
            found, found_cat, missed = 'a', biangle['a'], 'b'
        else:
            found, found_cat, missed = 'b', biangle['b'], 'a'
        missed_cat = round(((hip**2) - (found_cat**2))**0.5, 3)
        if missed_cat % int(missed_cat) == 0:
            missed_cat = int(missed_cat)
        triangle = {found:found_cat, missed:missed_cat, 'c':hip}
    else:
        a, b = biangle.values()
        c = ((a**2) + (b**2))**0.5
        triangle = biangle
        triangle.update({'c':c})
    return triangle

d={'a': 5, 'c': 13}
how_to_find_them(d)