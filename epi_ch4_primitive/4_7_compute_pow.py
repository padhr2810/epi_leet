
def power(x: float, y: int) -> float:
    print(f"\n\n##################################################################")
    print(f"POWER {x}, {y}")
    print(f"##################################################################")
    print(f"\nx {x} {bin(x)} ... y {y} {bin(y)}")

    result, power = 1.0, y
    print(f"initial power = {power}")
    if y < 0:
        power, x = -power, 1.0 / x
        print(f"as y is negative, adjusted power, x = {power}, {x}")

    print("\n######################\nSTART LOOP\n######################")
    loop_counter = 0
    while power:
        loop_counter += 1
        print(f"\nloop number: {loop_counter}")
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
        print(f"updated x, power, result = {x}, {power}, {result}")
    print(f"result = {result}")
    return result


power(2,2)
power(2,3)
power(4,2)
power(4,3)
