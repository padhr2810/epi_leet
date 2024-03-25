import functools
import string

#from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        print(f"\n###### Run construct_from_base ######")
        print(f"num_as_int // base = {num_as_int // base}")
        print(f"num_as_int % base = {num_as_int % base}")
        print(f"string.hexdigits[num_as_int % base].upper() = {string.hexdigits[num_as_int % base].upper()}")
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    print(f"same str to int as previous 6_1, but use 'hexdigits' here to generalise it")
    
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


if __name__ == '__main__':
    res255 = convert_base("255", 10, 2)
    res1000 = convert_base("1000", 10, 100)
    res100 = convert_base("100", 10, 100)
    print(f"res255 = {res255}") 
    print(f"res1000 = {res1000}") 
    print(f"res100 = {res100}") 
    
    print(string.hexdigits[2])
    print(string.hexdigits[4])
    print(string.hexdigits[11])
    #exit(
    #    generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
    #                                   convert_base))
