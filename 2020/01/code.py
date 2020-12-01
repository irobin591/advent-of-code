# Advent of Code 2020
# Day 01
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read()

# Prep Input
input_data = list(map(int, input_data.strip().split('\n')))
# print(input_data)


def part1(input_data):
    """
    >>> part1([1721,979,366,299,675,1456])
    514579
    """
    # Easy nested loop solution:
    # for entry1 in input_data:
    #     for entry2 in input_data:
    #         if entry1 + entry2 == 2020:
    #             return entry1 * entry2

    # Juggling with numbers
    # First: Sort the list
    data = input_data.copy()
    data.sort()

    # Select the smallest and the largest number
    left_el = 0
    right_el = len(data)-1

    # Decrease the largest number and increase the smallest number
    while True:
        if right_el < left_el:
            # We have missed the numbers (or there are none)
            return None

        el_sum = data[left_el] + data[right_el]

        if el_sum == 2020:
            return data[left_el] * data[right_el]

        if el_sum > 2020:
            # Select a smaller number to decrease the sum
            right_el -= 1
        else:
            # Select a bigger number to increase the sum
            left_el += 1
            

def part2(input_data):
    """
    >>> part2([1721,979,366,299,675,1456])
    241861950
    """
    for entry1 in input_data:
        for entry2 in input_data:
            for entry3 in input_data:
                if entry1 + entry2 + entry3 == 2020:
                    return entry1 * entry2 * entry3
    return None


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass