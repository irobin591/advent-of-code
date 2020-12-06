# Advent of Code 2020
# Day 06
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n\n')


def part1(input_data):
    """
    >>> part1(["abc"])
    3
    >>> part1(["a\\nb\\nc"])
    3
    >>> part1(["ab\\nac"])
    3
    >>> part1(["a\\na\\na\\na"])
    1
    >>> part1(["b"])
    1
    """
    total_count = 0
    for group in input_data:
        ppl = group.split('\n')
        yes_questions = {}
        for person in ppl:
            for answer in person:
                if not answer in yes_questions:
                    yes_questions[answer] = 0
                yes_questions[answer] += 1
        total_count += len(yes_questions)
    return total_count


def part2(input_data):
    """
    >>> part2(["abc"])
    3
    >>> part2(["a\\nb\\nc"])
    0
    >>> part2(["ab\\nac"])
    1
    >>> part2(["a\\na\\na\\na"])
    1
    >>> part2(["b"])
    1
    """
    total_count = 0
    for group in input_data:
        ppl = group.split('\n')
        yes_questions = {}
        for person in ppl:
            for answer in person:
                if not answer in yes_questions:
                    yes_questions[answer] = 0
                yes_questions[answer] += 1
        total_count += len(list(filter(lambda key: yes_questions[key] == len(ppl), yes_questions)))
    return total_count


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass