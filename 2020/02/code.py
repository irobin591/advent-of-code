# Advent of Code 2020
# Day 02
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def prep_data(input_data):
    # 0: min amount of char | no 1
    # 1: max amount of char | no 2
    # 2: char
    # 3: string
    re_input = re.compile(r'^([0-9]+)-([0-9]+) ([a-z]+): ([a-z]*)$')

    return list(map(lambda x: re_input.match(x).groups(), input_data))


def part1(input_data):
    """
    >>> part1(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"])
    2
    """
    input_data = prep_data(input_data)
    count = 0
    import collections
    for min_c, max_c, c, passwd in input_data:
        x = collections.Counter(passwd)[c]
        if x >= int(min_c) and x <= int(max_c):
            count += 1
    return count


def part2(input_data):
    """
    >>> part2(["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"])
    1
    """
    input_data = prep_data(input_data)
    count = 0
    for index1, index2, c, passwd in input_data:
        c1 = passwd[int(index1)-1]
        c2 = passwd[int(index2)-1]
        if sum([c1 == c, c2 == c]) == 1:
            count += 1
    return count


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass