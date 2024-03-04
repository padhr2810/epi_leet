

def multiply(x: int, y: int) -> int:
    print(f"\nStarting x = {x}")
    def add(a,b):
        while b:
            carry = a&b
            print(f"\ncarry = {carry}")
            a,b = a^b, carry << 1

            print(f"\na,b = a^b, carry << 1 = {a,b}")
        return a 
    
    running_sum = 0 
    counter=1
    while x: 
        print(f"\n########\ncounter = {counter}\n########")
        print(f"\nnew x = {x}")
        print(f"\nx&1 = {x&1}")
        if x&1:
            running_sum = add(running_sum,y)
        print(f"\nnew running sum = {running_sum}")
        x,y = x >> 1, y << 1 
        print(f"\nx,y = x >> 1, y << 1 = {x,y}")
    print(f"\nfinal running sum = {running_sum}")
    return running_sum

x1_5 = multiply(1, 5)
x2_5 = multiply(2, 5)
x11_123 = multiply(11, 123)
x_minus10_12 = multiply(-10, 12)
print(f"1 x 5 = {x1_5}")
print(f"2 x 5 = {x2_5}")
print(f"11 x 123 = {x11_123}")
print(f"-10 x 12 = {x_minus10_12}")
