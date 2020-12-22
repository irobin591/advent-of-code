# Advent of Code {{ YEAR }}
# Day {{ DAY }}
# Author: {{ AUTHOR }}

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\n'))
    None
    """
    return None


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part2.txt"), 'r').read().strip().split('\n'))
    None
    """
    return None


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass