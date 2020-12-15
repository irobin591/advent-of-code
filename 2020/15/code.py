# Advent of Code 2020
# Day 15
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = [int(x) for x in input_file.read().strip().split(',')]


def part1(input_data):
    """
    >>> part1([0,3,6])
    436
    >>> part1([1,3,2])
    1
    >>> part1([2,1,3])
    10
    >>> part1([1,2,3])
    27
    >>> part1([2,3,1])
    78
    >>> part1([3,2,1])
    438
    >>> part1([3,1,2])
    1836
    """
    memory = input_data.copy()
    for i in range(2020-len(input_data)):
        last = memory[-1]
        new_entry = 0
        len_memory = len(memory)
        for x in range(1, len_memory):
            if memory[len_memory-x-1] == last:
                new_entry = x
                break
        memory.append(new_entry)
    return memory[-1]


def part2(input_data):
    """
    >>> part2([0,3,6])
    175594
    >>> part2([1,3,2])
    2578
    >>> part2([2,1,3])
    3544142
    >>> part2([1,2,3])
    261214
    >>> part2([2,3,1])
    6895259
    >>> part2([3,2,1])
    18
    >>> part2([3,1,2])
    362
    """
    last_repeat = {}
    last_id = 0
    last_element = input_data[0]

    memory = [input_data[0]]

    for i, entry in enumerate(input_data):
        if i == 0:
            continue
        last_repeat[last_element] = last_id

        last_element = entry
        last_id = i
        memory.append(entry)

    import tqdm
    for i in tqdm.tqdm(range(len(input_data), 30000000)):
        new_entry = 0
        if last_element in last_repeat:
            new_entry = i - last_repeat[last_element] - 1

        last_repeat[last_element] = last_id

        memory.append(new_entry)
        last_element = new_entry
        last_id = i

        continue

        
        # new_entry = 0
        # len_memory = len(memory)
        # if last_element
        # for x in range(1, len_memory):
        #     if memory[len_memory-x-1] == last:
        #         new_entry = x
        #         break
        # memory.append(new_entry)
    return last_element


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass