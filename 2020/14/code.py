# Advent of Code 2020
# Day 14
# Author: irobin591

import os
import doctest
import re

re_mask = re.compile(r'^mask = ([01X]{36})$')
re_mem = re.compile(r'^mem\[([0-9]+)\] = ([0-9]+)$')

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","mem[8] = 11","mem[7] = 101","mem[8] = 0"])
    165
    """
    memory = dict()
    mask = "X" * 36

    for line in input_data:
        match_mask = re_mask.match(line)
        match_mem = re_mem.match(line)

        if match_mask:
            mask = match_mask.group(1)

        if match_mem:
            raw_data = int(match_mem.group(2))

            # or data with X being treated as 0 and not having an impact
            # x | 1 = x
            or_mask = int(mask.replace('X', '0'), 2)
            raw_data = raw_data | or_mask

            # and data with X being treated as 1 and not having an impact
            # x & 1 = x
            and_mask = int(mask.replace('X', '1'), 2)
            raw_data = raw_data & and_mask

            memory[int(match_mem.group(1))] = raw_data
    return sum(memory.values())


def part2(input_data):
    """
    >>> part2(["mask = 000000000000000000000000000000X1001X","mem[42] = 100","mask = 00000000000000000000000000000000X0XX","mem[26] = 1"])
    208
    """
    
    memory = dict()
    mask = "0" * 36

    for line in input_data:
        match_mask = re_mask.match(line)
        match_mem = re_mem.match(line)

        if match_mask:
            mask = match_mask.group(1)

        if match_mem:
            memory_spot = int(match_mem.group(1))
            data = int(match_mem.group(2))

            # Convert memory_spot to binary
            binary_data = "{:036b}".format(memory_spot)
            new_binary_data = []

            # Apply mask: Save 1, ignore 0 and save X
            for i, x in enumerate(mask):
                if x == '1' or x == 'X':
                    new_binary_data.append(x)
                elif x == '0':
                    new_binary_data.append(binary_data[i])
            
            # Recursively iterate though binary data
            def recursive_update(cur_binary_data, cur_el):
                # If we are at the end, convert binary data to int and save the data
                if cur_el >= len(cur_binary_data):
                    memory[int("".join(cur_binary_data), 2)] = data
                    return

                # If the current character is a 'X', duplicate the data and
                # replace the X with 0 and 1 and recursively continue on each dataset
                if cur_binary_data[cur_el] == 'X':
                    data_0 = cur_binary_data.copy()
                    data_0[cur_el] = '0'
                    recursive_update(data_0, cur_el+1)

                    data_1 = cur_binary_data.copy()
                    data_1[cur_el] = '1'
                    recursive_update(data_1, cur_el+1)
                else:
                    # If the current character is not a 'X', continue to the next character
                    recursive_update(cur_binary_data, cur_el+1)

            recursive_update(new_binary_data, 0)
    return sum(memory.values())


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass