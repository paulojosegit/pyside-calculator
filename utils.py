
import re

def isValidNumber(string: str):
    VALID_KEYS_REGEX = re.compile(r'^[0-9\/\*\-\+\.\^]')
    if VALID_KEYS_REGEX.findall(string):
        return VALID_KEYS_REGEX

def isEmpty(string: str):
    return len(string) == 0