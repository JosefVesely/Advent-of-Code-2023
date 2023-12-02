# --- Day 2: Cube Conundrum ---
import pprint

# Return game number if the game is possible
def solve_game(line: str) -> int:
    # Parse input
    game_number = int(line.split(" ")[1][:-1])

    sets = []
    set = {}

    for i, name in enumerate(line.split(" ")[2:]):
        if i % 2 == 0:
            set["number"] = int(name)
        else:
            set["color"] = name.replace(",", "").replace(";", "")
            sets.append(set)
            set = {}
        
        if name[-1] == ";":
            sets.append(0)

    sets.append(0)

    # Solve game
    red = BAG_RED = 12
    green = BAG_GREEN = 13
    blue = BAG_BLUE = 14

    for set in sets:
        if set != 0:
            if set["color"] == "red":
                red -= set["number"]
            elif set["color"] == "green":
                green -= set["number"]
            elif set["color"] == "blue":
                blue -= set["number"]

        if set == 0:
            if min(red, green, blue) < 0:
                return 0
            
            red = BAG_RED
            green = BAG_GREEN
            blue = BAG_BLUE

    return game_number

with open("input.txt", "r") as input:
    lines = input.readlines()

    sum = 0

    for line in lines:
        line = line.strip()
        sum += solve_game(line)

    print(sum)