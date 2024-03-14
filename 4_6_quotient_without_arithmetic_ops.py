

def divide(x: int, y: int) -> int:

    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result

print(f"4 / 2 = {divide(4,2)}")
print(f"5 / 2 = {divide(5,2)}")
print(f"10 / 2 = {divide(10,2)}")
