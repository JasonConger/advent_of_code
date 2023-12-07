from pathlib import Path
import re

symbols = ["*", "=", "-", "+", "&", "#", "%", "/", "@", "$"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

def convert2DArray(lines):

    grid = []
    for line in lines:

        # unpack the line into chars
        lineChars = [*line]

        # get rid of the newline
        if(lineChars[len(lineChars)-1] == '\n'):
             lineChars.pop()
        grid.append(lineChars)
    return grid

def get_adjacent(grid, x, y, value=None):
    
    adj = []
    for k in range(x-1,x+2):
        for l in range(y-1, y+2):
            if k in range(0,len(grid)) and l in range(0, len(grid[k])):
                adj.append(grid[k][l])
                if (value) and (grid[k][l] == value):
                    return (k,l)
    return adj

def add_gear(gears, key, value):
    if key in gears.keys():
        if value not in gears[key]:
            gears[key].append(value)
    else:
        gears[key] = [value]

def part1(grid, lines):

    total = 0
    line_number = 0

    for line in lines:

        # find the numbers in the line
        number_search = re.finditer(r'(\d+)', line)
        for number in number_search:
            
            # See if the start or end position of the number is adjacent to a symbol.
            # Note: the span property will contain the first and last position of the match.
            start = number.span()[0]
            end = number.span()[1] - 1

            adjacent_values = get_adjacent(grid, line_number, start)
            adjacent_values.extend(get_adjacent(grid, line_number, end))
            
            is_part_number = any(thing in adjacent_values for thing in symbols)

            if(is_part_number):
                total = total + int(number.group())
                continue

        line_number = line_number + 1
        
    return total

def part2(grid, lines):

    line_number = 0
    gears = {}
    ratio_sum = 0
    for line in lines:

        # find numbers
        number_search = re.finditer(r'(\d+)', line)
        for number in number_search:
            start = number.span()[0]
            end = number.span()[1] - 1
            n = int(number.group())

            # any "*" around here?
            adjacent_values_start = get_adjacent(grid, line_number, start)
            if('*' in adjacent_values_start):
                star_pos = get_adjacent(grid, line_number, start, "*")
                add_gear(gears, star_pos, n)
                 
            # any "*" around here?
            adjacent_values_end = get_adjacent(grid, line_number, end)
            if('*' in adjacent_values_end):
                star_pos = get_adjacent(grid, line_number, end, "*")
                add_gear(gears, star_pos, n)

        line_number = line_number + 1

    # we got a lit of all the potential gears, let's see if which gears have 2 numbers
    for k in gears.keys():
        if len(gears[k]) == 2:
            ratio = gears[k][0] * gears[k][1]
            ratio_sum = ratio_sum + ratio
    
    return ratio_sum

if __name__ == "__main__":

    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        lines = f.readlines()

    # convert the text into a 2d array
    grid = convert2DArray(lines)

    print(part1(grid, lines))
    print(part2(grid, lines))