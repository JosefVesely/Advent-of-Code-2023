# --- Day 4: Scratchcards ---

def scratch_card(line: str) -> int:
    # Parse winning numbers
    winning_numbers_str = line.replace("  ", " ").split("|")[0].split(":")[1].strip().split(" ")
    winning_numbers = [int(i) for i in winning_numbers_str]

    # Parse ticket numbers
    ticket_numbers_str = line.replace("  ", " ").split("|")[1].strip().split(" ")
    ticket_numbers = [int(i) for i in ticket_numbers_str]

    match_count = len(list(set(winning_numbers) & set(ticket_numbers)))

    # Calculate points
    total_points = 0
    point_value = 1

    for i in range(match_count):
        total_points += point_value
        
        if i != 0:
            point_value *= 2

    return total_points


with open("input.txt", "r") as input:
    lines = input.readlines()

    total_points = 0

    for i, line in enumerate(lines):
        line = line.strip()
        total_points += scratch_card(line)
    
    print(f"{total_points=}")