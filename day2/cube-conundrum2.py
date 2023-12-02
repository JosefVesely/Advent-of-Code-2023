# --- Day 2: Cube Conundrum (Part Two) ---

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
    lowest_red = 0
    lowest_green = 0
    lowest_blue = 0

    for set in sets:
        if set != 0:
            if set["color"] == "red":
                lowest_red = set["number"] if set["number"] > lowest_red else lowest_red
            elif set["color"] == "green":
                lowest_green = set["number"] if set["number"] > lowest_green else lowest_green
            elif set["color"] == "blue":
                lowest_blue = set["number"] if set["number"] > lowest_blue else lowest_blue

    return lowest_red*lowest_green*lowest_blue

with open("input.txt", "r") as input:
    lines = input.readlines()

    sum = 0

    for line in lines:
        line = line.strip()
        sum += solve_game(line)

    print(sum)