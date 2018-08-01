from itertools import combinations

def buy_newspaper(s1, s2):
    for s in set(s2):
        if s not in s1:
            return -1
    stopper = len(s1)
    journals = 0
    while stopper > 0:
        x = map(lambda x: ''.join(x), combinations(s1, stopper))
        for template in x:
            journals += s2.count(template)
            s2 = s2.replace(template, '')
        stopper -= 1
    return journals