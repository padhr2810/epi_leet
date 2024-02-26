

print("\nParity of binary word is 1 if odd number of 1s. Otherwise 0\n")

def parity_brute_force(input_value: int) -> int:
    result = 0
    counter = 1 
    while input_value:
        print(f"\n\n######################## \n ITERATION # {counter}\
        \n########################\n")

        print(f"\ninput_value before update = {input_value} / {bin(input_value)}")
        print(f"\nLen of binary input: {len(bin(input_value))-2}")
        print(f"\nresult before update = {result}")
        
        
        result ^=  input_value & 1 
        ###### THE CRITICAL LINE. IF RESULT =1, A VALUE OF 1 SENDS IT BACK TO 0
        ###### IF RESULT =0, A VALUE OF 1 SENDS IT UP TO 1.
        ###### A VALUE OF 0 HAS NO EFFECT.
        
        
        print(f"\ninput_value & 1 = {input_value & 1}")
        print(f"\nresult AFTER update = {result}")

        input_value >>= 1
        ## i.e. drop the first digit in binary word.
        print(f"\ninput_value after update = {input_value}")
        counter += 1

    return result 



print(f"Parity of 21 = { parity_brute_force(21) }") 


print("#####################################################################################")
six_parity =  parity_brute_force(6)
five_parity =  parity_brute_force(5)
four_parity =  parity_brute_force(4)
three_parity =  parity_brute_force(3)
two_parity =  parity_brute_force(2)
one_parity =  parity_brute_force(1)
zero_parity =  parity_brute_force(0)
seven_parity =  parity_brute_force(7)

print(f"Parity of 7 / {bin(7)} = { seven_parity }") 
print(f"Parity of 6 / {bin(6)} = { six_parity }") 
print(f"Parity of 5 / {bin(5)} = { five_parity }") 
print(f"Parity of 4 / {bin(4)} = { four_parity }") 
print(f"Parity of 3 / {bin(3)} = { three_parity }") 
print(f"Parity of 2 / {bin(2)} = { two_parity }") 
print(f"Parity of 1 / {bin(1)} = { one_parity }") 
print(f"Parity of 0 / {bin(0)} = { zero_parity }") 

three_1s = int('111', 2)
two_1s = int('110', 2)
print(f"three_1s = {three_1s}")
print(f"two_1s = {two_1s}")
