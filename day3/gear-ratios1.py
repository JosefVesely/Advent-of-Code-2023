# --- Day 3: Gear Ratios ---

import re

class FoundNumber:
    def __init__(self, y, span: tuple[int, int]):
        self.y = y
        self.span = span

    def __eq__(self, other):
        if isinstance(other, FoundNumber):
            return self.y == other.y and self.span == other.span
        return False

def find_number(map, x, y):
    line = "".join(map[y])

    for m in re.finditer("[0-9]+", line):
        number = int(m.group())

        if x in range(m.start(), m.end()):
            if FoundNumber(y, m.span()) in found_numbers:
                return 0
            else:
                found_numbers.append(FoundNumber(y, m.span()))
        
            return number
        
    return 0


with open("input.txt", "r") as input:
    map = [[c for c in line.strip()] for line in input]


global found_numbers
found_numbers = []
numbers = []

for y, row in enumerate(map):
    for x, char in enumerate(row):
        if not char.isdigit() and char != ".":  # Symbol - gear
            # chars around
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue

                    if map[y+i][x+j].isdigit():
                        numbers.append(find_number(map, x+j, y+i))

print(f"{sum(numbers)=}")