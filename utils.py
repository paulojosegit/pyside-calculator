
import re

DISPLAY_REGEX = re.compile(r'^[0-9+\-*/.=\^]+$')

def validDisplay(string):
    if DISPLAY_REGEX.search(string):
        return string

def validatorDisplay(string):
    if string[0] == '=' and string[-1] == '=':
        return
