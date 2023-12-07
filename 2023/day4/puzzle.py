from pathlib import Path
import re

card_numbers = []

def part1(lines):

    point_total = 0

    for line in lines:
        
        cards = re.search(r'^.+:\s(.*)\|(.*)', line)
        winning_cards = cards.groups()[0].split()
        winning_cards = set(map(int, winning_cards))
        my_cards = cards.groups()[1].split()
        my_cards = set(map(int, my_cards))
        
        my_winning_cards = winning_cards & my_cards

        if len(my_winning_cards) > 0:
            card_total = 2 ** (len(my_winning_cards) - 1)
            point_total = point_total + card_total

    return point_total

def get_winning_cards(lines, start, end):

    for line in range(start, end):
        card_num = re.search(r'^Card\s+(\d+):', lines[line]).group(1)
        my_winning_total = get_winning_total(lines[line])
        card_numbers.append(card_num )

        # check the next cards
        get_winning_cards(lines, line+1, line + 1 + len(my_winning_total))

def get_winning_total(line):
    cards = re.search(r'^.+:\s(.*)\|(.*)', line)
    winning_cards = cards.groups()[0].split()
    winning_cards = set(map(int, winning_cards))
    my_cards = cards.groups()[1].split()
    my_cards = set(map(int, my_cards))
    my_winning_total = winning_cards & my_cards
    return my_winning_total

def part2(lines):

    for line in range(0, len(lines)):

        card_num = re.search(r'^Card\s+(\d+):', lines[line]).group(1)
        my_winning_total = get_winning_total(lines[line])

        card_numbers.append(card_num )

        # check the next cards
        get_winning_cards(lines, line+1, line + 1 + len(my_winning_total))
            
            

    return len(card_numbers)

if __name__ == "__main__":

    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        lines = f.readlines()

    #print(part1(lines))
    print(part2(lines))