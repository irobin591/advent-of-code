# Advent of Code {{ YEAR }}
# Day {{ DAY }}
# Author: {{ AUTHOR }}

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read()

# Prep Input
# input_data = list(map(int, input_data.strip().split('\n')))


def part1():
    """
    >>> part1()
    None
    """
    return None


def part2():
    """
    >>> part2()
    None
    """
    return None


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1()))
    print("Part Two: {}".format(part2()))
    pass