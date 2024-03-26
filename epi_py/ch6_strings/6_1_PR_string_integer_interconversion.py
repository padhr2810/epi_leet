from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    if x == 0:
        return "0"
    if x < 0:
        x = -x 
        neg = True 
    else:
        neg = False 
        
    res = ""
    while x:
        i = x % 10
        res += chr(i + ord("0"))
        x //= 10
        

    res = "".join(reversed(res))
    if neg:
        res = "-" + res 
    return res 


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    if s == "0":
        return 0
    if s[0] == "-":
        neg = True 
        s = s[1:]
    elif s[0] == "+": 
        neg = False
        s = s[1:]
    else: 
        neg = False 

    print(f"Input = {s}")
    print(f"ord('0') = {ord('0')}")
    res = 0
    for ch in s:
        res *= 10
        print(f"char = {ch}; Unicode int for ch = {ord(ch)}")
        res += (ord(ch) - ord("0"))
    if neg: 
        res = -res 
    return res 


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
