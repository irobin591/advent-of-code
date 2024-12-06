# Advent of Code 2024
# Day 04
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

def check_xmas(data, search, x, y, dx, dy) -> int:
    if not search:
        return 1
    if x < 0 or x >= len(data):
        return 0
    if y < 0 or y >= len(data[x]):
        return 0
    if data[x][y] == search[0]:
        return check_xmas(data, search[1:], x + dx, y + dy, dx, dy)
    
    return 0

def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    18
    """

    count = 0

    for x, line in enumerate(input_data):
        for y, char in enumerate(line):
            if char == 'X':
                # Check all directions
                count += check_xmas(input_data, 'XMAS', x, y, -1, -1)
                count += check_xmas(input_data, 'XMAS', x, y, -1,  0)
                count += check_xmas(input_data, 'XMAS', x, y, -1,  1)
                count += check_xmas(input_data, 'XMAS', x, y,  0, -1)
                count += check_xmas(input_data, 'XMAS', x, y,  0,  1)
                count += check_xmas(input_data, 'XMAS', x, y,  1, -1)
                count += check_xmas(input_data, 'XMAS', x, y,  1,  0)
                count += check_xmas(input_data, 'XMAS', x, y,  1,  1)

    return count


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    9
    """

    count = 0

    for x, line in enumerate(input_data):
        for y, char in enumerate(line):
            if char == 'A':
                found_mas = 0
                # Check all directions
                found_mas += check_xmas(input_data, 'MAS', x+1, y+1, -1, -1)
                found_mas += check_xmas(input_data, 'MAS', x+1, y-1, -1,  1)
                found_mas += check_xmas(input_data, 'MAS', x-1, y+1,  1, -1)
                found_mas += check_xmas(input_data, 'MAS', x-1, y-1,  1,  1)

                if found_mas == 2:
                    count += 1
    return count


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass