# Advent of Code 2020
# Day 10
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = [int(x) for x in input_file.read().strip().split('\n')]


def sliding_window(iterable, size):
    window = []
    for item in iterable:
        window.append(item)
        if len(window) == size:
            yield tuple(window)
            window.pop(0)


def part1(input_data):
    """
    >>> part1([16,10,15,5,1,11,7,19,6,12,4])
    35
    >>> part1([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
    220
    """
    # Add 0 as the source outlet
    # Add max+3 as the device's built-in adapter
    input_data = input_data.copy()
    input_data.append(0)
    input_data.append(max(input_data)+3)

    input_data.sort()

    # print(input_data)

    windows = list(sliding_window(input_data, 2))

    differences = [b-a for a,b in windows]

    one_jolt_diffs = len(list(filter(lambda x: x == 1, differences)))
    three_jolt_diffs = len(list(filter(lambda x: x == 3, differences)))
    return one_jolt_diffs * three_jolt_diffs


def part2(input_data):
    """
    >>> part2([16,10,15,5,1,11,7,19,6,12,4])
    8
    >>> part2([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
    19208
    """
    input_data = input_data.copy()
    input_data.append(0)
    input_data.append(max(input_data)+3)

    input_data.sort()
    input_data.reverse()
    # print(input_data)

    # Go through the list backwards
    # Count the amount of possibilities to reach the last outlet from outlet i
    # Init: 1 possibility to reach the last outlet from the last outlet
    # For each further outlet:
    #   check the 3 higher outlets if they are in reach (less then 3 jolts away)
    #   for each higher outlet near enough:
    #       Add amount of possibilities from higher outlet to the end
    repeated = [1]
    for i, num in enumerate(input_data):
        if i == 0:
            continue
        repeated.append(0)
        for prev_i in [i-1,i-2,i-3]:
            # Check the 3 "higher" outlets if they are within reach of the current outlet
            if prev_i >= 0 and input_data[prev_i]-3 <= num:
                # Add possibilities from outlet prev_i to the end to the total for this
                repeated[i] += repeated[prev_i]

    # print(repeated)
    # Return the last element: amount of possibilities from the first element to reach the last element
    return repeated[-1]


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass