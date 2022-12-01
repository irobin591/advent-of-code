# Advent of Code 2022
# Day 01
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    24000
    """
    cur_cal = 0
    max_cal = 0

    for line in input_data:
        if line == '':
            max_cal = max(cur_cal, max_cal)
            cur_cal = 0
        else:
            cur_cal += int(line)

    max_cal = max(cur_cal, max_cal)

    return max_cal


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    45000
    """
    calories = []
    cur_cal = 0

    for line in input_data:
        if line == '':
            calories.append(cur_cal)
            cur_cal = 0
        else:
            cur_cal += int(line)

    calories.append(cur_cal)

    calories.sort()

    return calories[-1] + calories[-2] + calories[-3]


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass