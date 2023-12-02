# --- Day 1: Trebuchet?! ---

def get_calibration_number(line: str) -> int:
    # Find first digit
    for char in line:
        if char.isdigit():
            first_digit = char
            break

    # Find last digit
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break

    # Return calibration number
    return int(first_digit + last_digit)


with open("input.txt", "r") as input:
    lines = input.readlines()

    sum = 0

    for line in lines:
        line = line.strip()
        sum += get_calibration_number(line)

    print(sum)