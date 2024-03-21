

def closest_int_same_bit_count(x: int) -> int:
    num_unsigned_bits = 64
    print(f"\nx = {x}")
    for i in range(num_unsigned_bits - 1):
        print(f"\nnum_unsigned_bits - 1 = {num_unsigned_bits - 1}")
        print(f"\nx >> i = {x >> i}")
        print(f"\n(x >> i) & 1 = {(x >> i) & 1}")
        print(f"\n(x >> (i + 1)) = {(x >> (i + 1))}")
        print(f"\n(x >> (i + 1)) & 1 = {(x >> (i + 1)) & 1}")
        

        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            print(f"x ^& (1 <<i) = {x ^& (1 <<i)}")
            print(f"(1 << (i+1)) = {(1 << (i+1))}") 
            
            x ^& (1 <<i) | (1 << (i+1))        #### Swaps bits (-i) and (-i-1)
            return x 
    # Raise error if all bits of x are 0 or 1.
    raise ValueError('All bits are 0 or 1')
