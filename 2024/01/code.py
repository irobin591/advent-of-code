# Advent of Code 2024
# Day 01
# Author: irobin591

import os
import doctest
import collections

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    11
    """

    list1 = []
    list2 = []

    for line in input_data:
        d = line.split(' ', 1)
        d1, d2 = d

        list1.append(int(d1.strip()))
        list2.append(int(d2.strip()))


    list1.sort()
    list2.sort()

    target = 0

    for i in range(len(list1)):
        target += abs(list1[i] - list2[i])

    return target


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    31
    """
    list1 = []
    list2 = []

    for line in input_data:
        d = line.split(' ', 1)
        d1, d2 = d

        list1.append(int(d1.strip()))
        list2.append(int(d2.strip()))


    list1.sort()
    counter = collections.Counter(list2)

    target = 0

    for entry in list1:
        target += entry * counter.get(entry, 0)

    return target


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass