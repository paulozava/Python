
class A():
    @staticmethod
    def a_method():
        print('A method')

class B():
    @staticmethod
    def other_method():
        print('Other method')

class C(A, B):
    pass


def generation(data):
    for item in data:
        yield item

from datetime import date

niver = date(1987, 8, 15)
tod = date.today()
dias = tod - niver
print(dias)

niver + 15100


from timeit import Timer

def for_loop(t, n=0):
    try:
        a = 0
        for i in t:
            i /= 1.0
            a += i ** i
            n += 1
        return a
    except:
        print(n)

def rec_loop(t, a=1, n=0):
    try:
        if t:
            el = t.pop() / 1.0
            a += el ** el
            n +=1
            return rec_loop(t, a=a, n=n)
        else:
            return a
    except:
        print(n)

t = list(range(145))
for_loop(t)
rec_loop(t)
Timer('for_loop(t)', 'rec_loop(t)').timeit()

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)


from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)

round(.70 * 1.05, 2)

