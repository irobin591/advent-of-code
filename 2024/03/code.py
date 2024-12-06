# Advent of Code 2024
# Day 03
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    161
    """

    p = re.compile('mul\(\d{1,3},\d{1,3}\)')
    p2 = re.compile('mul\((\d{1,3}),(\d{1,3})\)')

    sum_data = 0

    for text in input_data:
        for entry in p.findall(text):
            r = p2.match(entry)
            sum_data += int(r.group(1)) * int(r.group(2))

    return sum_data


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part2.txt"), 'r').read().strip().split('\\n'))
    48
    """

    p = re.compile('(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))')
    p2 = re.compile('mul\((\d{1,3}),(\d{1,3})\)')

    sum_data = 0
    enabled = 1

    for text in input_data:
        for entry in p.findall(text):
            if entry == 'do()':
                enabled = 1
            elif entry == 'don\'t()':
                enabled = 0
            else:
                r = p2.match(entry)
                sum_data += int(r.group(1)) * int(r.group(2)) * enabled
    return sum_data


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass