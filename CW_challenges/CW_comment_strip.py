# a function that receive a string an some markers and return this string without this markers

def solution(string,markers):
    parts = string.split('\n')
    for mark in markers:
        parts = [part.split(mark)[0].rstrip() for part in parts]
    return '\n'.join(parts)