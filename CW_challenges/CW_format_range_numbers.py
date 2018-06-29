# algorithm that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

def solution(args):
    begin, rest = args[0], args[1:]
    ender = []
    answer = str(begin)
    for number in rest:
        begin += 1
        if number != begin:
            if ender:
                answer, ender = check_ender(answer, ender)
            answer += ', {}'.format(number)
            begin = number
        else:
            ender.append(number)
    if ender:
        answer, ender = check_ender(answer, ender)
    return answer


def check_ender(answer, ender):
    if len(ender) > 1:
        answer += '-{}'.format(ender[-1])
    else:
        answer += ', {}'.format(*ender)
    ender = []
    return answer, ender