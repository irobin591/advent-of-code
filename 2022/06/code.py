# Advent of Code 2022
# Day 06
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip()


def part1(input_data):
    """
    >>> part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    7
    >>> part1('bvwbjplbgvbhsrlpgdmjqwftvncz')
    5
    >>> part1('nppdvjthqldpwncqszvftbrmjlhg')
    6
    >>> part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    10
    >>> part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    11
    """

    for i in range(len(input_data) - 3):
        if (len(set(input_data[i: i + 4])) == 4):
            return i+4
    return None


def part2(input_data):
    """
    >>> part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    19
    >>> part2('bvwbjplbgvbhsrlpgdmjqwftvncz')
    23
    >>> part2('nppdvjthqldpwncqszvftbrmjlhg')
    23
    >>> part2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    29
    >>> part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    26
    """

    for i in range(len(input_data) - 13):
        if (len(set(input_data[i: i + 14])) == 14):
            return i+14
    return None


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass