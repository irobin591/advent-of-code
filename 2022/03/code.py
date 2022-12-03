# Advent of Code 2022
# Day 03
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    157
    """

    sum = 0

    for line in input_data:
        size = len(line)
        p1 = set(line[:size//2])
        p2 = set(line[(size//2):])

        intersection = p1.intersection(p2)

        duplicate_char = intersection.pop()

        char_value = ord(duplicate_char) - ord('A') if duplicate_char.isupper() else ord(duplicate_char) - ord('a')

        sum += char_value + 1 + (26 if duplicate_char.isupper() else 0)

    return sum


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    70
    """

    sum = 0
    for group in chunks(input_data, 3):
        intersection = None
        for line in group:
            if intersection is None:
                intersection = set(line)
            else:
                intersection = intersection.intersection(set(line))
        
        common_char = intersection.pop()

        char_value = ord(common_char) - ord('A') if common_char.isupper() else ord(common_char) - ord('a')

        sum += char_value + 1 + (26 if common_char.isupper() else 0)
    return sum


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass