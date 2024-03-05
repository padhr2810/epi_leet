

def multiply_non_negatives(x: int, y: int) -> int:
    """
    Enters into an infinit loop if try with a NEGATIVE number!!
    Set up an assert to avoid this.
    """
    
    assert x >= 0   # critical !!
    assert y >= 0
    
    print(f"\n\n##########################\n##########################\n##########################\n")
    print(f"\nInputs x, y = {x, y}")
    print(f"\nbinary x, y = {bin(x), bin(y)}")
    def add(a,b):
        while b:
            carry = a&b
            print(f"\ncarry = {carry} ...... binary = {bin(carry)}")
            a,b = a^b, carry << 1

            print(f"\na,b = a^b, carry << 1 ........... {a,b}")
        return a 
    
    running_sum = 0 
    number_of_iterations=1
    while x: 
        print(f"\n########\nIteration = {number_of_iterations}\n########")
        print(f"\nnew x = {x} ... binary {bin(x)}")
        print(f"\nnew y = {y} ... binary {bin(y)}")
        print(f"\nx&1 = {x&1} ... binary {bin(x&1)}")
        if x&1:
            running_sum = add(running_sum,y)
        print(f"\nnew running sum = {running_sum} ... {bin(running_sum)}")
        x,y = x >> 1, y << 1 
        print(f"\nx,y = x >> 1, y << 1 ........... = {x,y}... bin {bin(x), bin(y)}")
        number_of_iterations+=1
    print(f"\nfinal running sum = {running_sum}")
    return running_sum, number_of_iterations

x1_5, iters_1_5 = multiply_non_negatives(1, 5)
x2_5, iters_2_5 = multiply_non_negatives(2, 5)
x11_10, iters_11_10 = multiply_non_negatives(11, 10)
x100_100, iters_100_100 = multiply_non_negatives(100, 100)
x255_255, iters_255_255 = multiply_non_negatives(255, 255)
x1million_1million, iters_1million_1million = multiply_non_negatives(1000000, 1000000)

print(f"1 x 5 = {x1_5} ... after {iters_1_5} iterations") 
print(f"2 x 5 = {x2_5} ... after {iters_2_5} iterations")
print(f"11 x 10 = {x11_10} ... after {iters_11_10} iterations")
print(f"100 x 100 = {x100_100} ... after {iters_100_100} iterations")
print(f"255 x 255 = {x255_255} ... after {iters_255_255} iterations")
print(f"1 million x 1 million = {x1million_1million} ... after {iters_1million_1million} iterations")


