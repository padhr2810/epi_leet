

import math


def is_palindrome_number(x: int) -> bool:

    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    print(f"num_digits = {num_digits}")
    
    msd_mask = 10**(num_digits - 1)
    print(f"msd_mask = {msd_mask}")
    
    loop_counter=0
    for i in range(num_digits // 2):
        loop_counter += 1
        print(f"\n### Loop number: {loop_counter}")
        print(f"x // msd_mask = {x // msd_mask}")
        print(f"x % 10 = {x % 10}")
        
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask  # Remove the most significant digit of x.
        print(f"x after remove msd = {x}")
        x //= 10  # Remove the least significant digit of x.
        print(f"x after remove lsd = {x}")
        msd_mask //= 100
        print(f"new msd_mask = {msd_mask}")
    return True

print(f"is_palindrome_number 33 = {is_palindrome_number(33)}")
print(f"is_palindrome_number 31 = {is_palindrome_number(31)}")
print(f"is_palindrome_number 12321 = {is_palindrome_number(12321)}")
print(f"is_palindrome_number -33 = {is_palindrome_number(-33)}")
