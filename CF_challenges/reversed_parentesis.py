import re

def invert_parentesis(string):
    re.findall(r'\((^\(\))\)', string)
    re.findall(r'\((\w+\s*)\)', string)