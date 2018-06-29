#a function that takes a positive integer number and returns the next bigger number formed by the same digits.

def next_bigger(number):
    matcher = sorted([match for match in str(number)])
    tester = ''.join(sorted(matcher, reverse=True))

    if len(matcher) <= 1 or tester == str(number):
        return -1

    endless_stopper = number * 10
    while True:
        number += 1
        tester = sorted([test for test in str(number)])
        if tester == matcher:
            return number
        if number == endless_stopper:
            return -1