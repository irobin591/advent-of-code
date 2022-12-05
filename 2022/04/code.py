# Advent of Code 2022
# Day 04
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    2
    """
    count = 0

    for line in input_data:
        x = re.search("^(\d+)-(\d+),(\d+)-(\d+)$", line)

        start1, end1, start2, end2 = x.groups()
        start1 = int(start1)
        end1 = int(end1)
        start2 = int(start2)
        end2 = int(end2)

        if (start1 >= start2 and end1 <= end2):
            count += 1
        elif (start1 <= start2 and end1 >= end2):
            count += 1

    return count


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    4
    """
    count = 0

    for line in input_data:
        x = re.search("^(\d+)-(\d+),(\d+)-(\d+)$", line)

        start1, end1, start2, end2 = x.groups()
        start1 = int(start1)
        end1 = int(end1)
        start2 = int(start2)
        end2 = int(end2)

        if (start1 > end2):
            continue

        if (start2 > end1):
            continue

        count += 1

    return count

if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass