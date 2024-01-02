# Advent of Code 2023
# Day 02
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    8
    """

    result = 0

    for line in input_data:
        game, draw = line.split(': ')
        max_color = {}

        game_id = int(game[5:])

        rounds = draw.split('; ')

        max_color['red'] = 0
        max_color['green'] = 0
        max_color['blue'] = 0

        for round in rounds:
            draws = round.split(', ')

            for draw in draws:
                amount, color = draw.split(' ')

                max_color[color] = max(int(amount), max_color[color])

        if max_color['red'] <= 12 and max_color['green'] <= 13 and max_color['blue'] <= 14:
            result += game_id
            
    return result


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    2286
    """

    result = 0

    for line in input_data:
        game, draw = line.split(': ')
        max_color = {}

        game_id = int(game[5:])

        rounds = draw.split('; ')

        max_color['red'] = 0
        max_color['green'] = 0
        max_color['blue'] = 0

        for round in rounds:
            draws = round.split(', ')

            for draw in draws:
                amount, color = draw.split(' ')

                max_color[color] = max(int(amount), max_color[color])

        power = max_color['red'] * max_color['green'] * max_color['blue']
        
        result += power

    return result


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass