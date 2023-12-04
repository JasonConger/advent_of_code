from pathlib import Path
import re

cubes_in_bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}



def part1(lines):

    possible_games = 0

    for line in lines:
        game_id = re.search(r'^Game\s(\d+):', line).group(1)
        reds = re.findall(r'(\d+)\s+red', line)
        reds = list(map(int, reds))
        greens = re.findall(r'(\d+)\s+green', line)
        greens = list(map(int, greens))
        blues = re.findall(r'(\d+)\s+blue', line)
        blues = list(map(int, blues))

        red_max = max(reds)
        green_max = max(greens)
        blue_max = max(blues)

        if (red_max <= cubes_in_bag["red"]) and (green_max <= cubes_in_bag["green"]) and (blue_max <= cubes_in_bag["blue"]):
            possible_games = possible_games + int(game_id)

    return possible_games


def part2(lines):

    power_sum = 0

    for line in lines:
        game_id = re.search(r'^Game\s(\d+):', line).group(1)
        reds = re.findall(r'(\d+)\s+red', line)
        reds = list(map(int, reds))
        greens = re.findall(r'(\d+)\s+green', line)
        greens = list(map(int, greens))
        blues = re.findall(r'(\d+)\s+blue', line)
        blues = list(map(int, blues))

        red_max = max(reds)
        green_max = max(greens)
        blue_max = max(blues)

        line_power = red_max * green_max * blue_max

        power_sum = power_sum + line_power

    return power_sum

if __name__ == "__main__":

    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        lines = f.readlines()

    print(part1(lines))
    print(part2(lines))