# --- Day 1: Trebuchet?! (Part Two) ---

def get_calibration_number(line: str) -> int:
    replacement_digits = {
        "one":   "o1e",
        "two":   "t2o",
        "three": "t3ree",
        "four":  "f4ur",
        "five":  "f5ve",
        "six":   "s6x",
        "seven": "s7ven",
        "eight": "e8ght",
        "nine":  "n9ne"
    }

    # Replace words with digits
    for key, value in replacement_digits.items():
        line = line.replace(key, value)

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