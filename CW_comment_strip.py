def solution(string,markers):
    parts = string.split('\n')
    for mark in markers:
        parts = [part.split(mark)[0].rstrip() for part in parts]
    return '\n'.join(parts)