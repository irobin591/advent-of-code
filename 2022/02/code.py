# Advent of Code 2022
# Day 02
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    15
    """

    def score(a, b):
        shape_selection = {'X': 1, 'Y': 2, 'Z': 3}[b]

        score = {
            # Draw
            'AX': 3,
            'BY': 3,
            'CZ': 3,
            # Win:
            'AY': 6,
            'BZ': 6,
            'CX': 6,
            # Lose
            'AZ': 0,
            'BX': 0,
            'CY': 0,
        }[a + b]

        return shape_selection + score
    
    total_score = 0
    for line in input_data:
        a, b = line.split(' ')
        total_score += score(a, b)
        
    return total_score


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    12
    """
    def score(a, b):
        score = {'X': 0, 'Y': 3, 'Z': 6}[b]

        shape_selection = {
            # Lose
            'AX': 3,
            'BX': 1,
            'CX': 2,
            # Draw
            'AY': 1,
            'BY': 2,
            'CY': 3,
            # Win:
            'AZ': 2,
            'BZ': 3,
            'CZ': 1,
        }[a + b]

        return shape_selection + score
    
    total_score = 0
    for line in input_data:
        a, b = line.split(' ')
        total_score += score(a, b)
        
    return total_score


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass