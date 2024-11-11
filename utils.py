
import re

DISPLAY_REGEX = re.compile(r'^[0-9+\-*/.]+$')

def validDisplay(string):
    if DISPLAY_REGEX.search(string):
        return string

