# Advent of Code 2023
# Day 01
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    142
    """
    sum = 0

    for line in input_data:
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                last_digit = int(char)
                first_digit = last_digit if first_digit is None else first_digit
        sum += first_digit * 10 + last_digit

    return sum


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part2.txt"), 'r').read().strip().split('\\n'))
    281
    """
    sum = 0

    for line in input_data:
        first_digit = None
        last_digit = None

        # Replace written out numbers
        line = line.replace('one', 'one1one')
        line = line.replace('two', 'two2two')
        line = line.replace('three', 'three3three')
        line = line.replace('four', 'four4four')
        line = line.replace('five', 'five5five')
        line = line.replace('six', 'six6six')
        line = line.replace('seven', 'seven7seven')
        line = line.replace('eight', 'eight8eight')
        line = line.replace('nine', 'nine9nine')

        for char in line:
            if char.isdigit():
                last_digit = int(char)
                first_digit = last_digit if first_digit is None else first_digit
        sum += first_digit * 10 + last_digit
        # print(first_digit * 10 + last_digit)

    return sum


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass