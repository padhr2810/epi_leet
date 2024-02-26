

def parity(input_value: int) -> int:
    result = 0
    counter = 1 
    while input_value:
        print(f"\n\n######################## \n ITERATION # {counter}\
        \n########################\n")

        print(f"\ninput_value before update = {input_value} / {bin(input_value)}")

        print(f"\nresult before update = {result}")
        result ^=  input_value & 1 
        print(f"\ninput_value & 1 = {input_value & 1}")
        print(f"\nresult AFTER update = {result}")

        input_value >>= 1
        print(f"\ninput_value after update = {input_value}")
        counter += 1

    return result 


r = parity(21)
