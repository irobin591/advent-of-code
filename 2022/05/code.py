# Advent of Code 2022
# Day 05
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().split('\\n'))
    'CMZ'
    """

    # Prepare stacks
    reverse_stack_configuration = []

    for line in input_data:
        # Abort if we hit the splitting line
        if line == '':
            break
        reverse_stack_configuration.append(line)

    number_row = reverse_stack_configuration.pop()
    stack_count = len(number_row.split('   '))

    stacks = {x: [] for x in range(stack_count)}

    # Iterate though the stacks backwards:
    for line in reverse_stack_configuration[::-1]:
        for i in range(stack_count):
            char = line[(i*4)+1:(i*4)+2]

            if char != ' ' and char != '':
                stacks[i].append(char)

    # Iterate though steps
    post_steps = False

    for line in input_data:
        # Continue after empty line
        if line == '':
            post_steps = True
            continue

        if not post_steps:
            continue

        x = re.search("^move (\d+) from (\d+) to (\d+)$", line)

        num, from_stack, to_stack = x.groups()

        for _ in range(int(num)):
            el = stacks[int(from_stack)-1].pop()
            stacks[int(to_stack)-1].append(el)

    result = ''

    for stack in stacks.values():
        result += stack.pop()

    return result


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().split('\\n'))
    'MCD'
    """

    # Prepare stacks
    reverse_stack_configuration = []

    for line in input_data:
        # Abort if we hit the splitting line
        if line == '':
            break
        reverse_stack_configuration.append(line)

    number_row = reverse_stack_configuration.pop()
    stack_count = len(number_row.split('   '))

    stacks = {x: [] for x in range(stack_count)}

    # Iterate though the stacks backwards:
    for line in reverse_stack_configuration[::-1]:
        for i in range(stack_count):
            char = line[(i*4)+1:(i*4)+2]

            if char != ' ' and char != '':
                stacks[i].append(char)

    # Iterate though steps
    post_steps = False

    for line in input_data:
        # Continue after empty line
        if line == '':
            post_steps = True
            continue

        if not post_steps:
            continue

        x = re.search("^move (\d+) from (\d+) to (\d+)$", line)

        num, from_stack, to_stack = x.groups()

        crane_buffer = []
        for _ in range(int(num)):
            crane_buffer.append(stacks[int(from_stack)-1].pop())

        for x in crane_buffer[::-1]:
            stacks[int(to_stack)-1].append(x)

    result = ''

    for stack in stacks.values():
        result += stack.pop()

    return result


if __name__ == "__main__":
    doctest.testmod()
    #print(part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n')))
    #print("Part One: {}".format(part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))))
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass