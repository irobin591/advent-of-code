# Advent of Code 2020
# Day 23
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip()


class Cup():
    def __init__(self, cup_id):
        self.id = cup_id
        self.next_cup = None


def part1(input_data):
    """
    >>> part1("389125467")
    '67384529'
    """
    # SLOW VERSION
    # # First cup = current cup
    # cups = list(map(int, input_data))

    # size = len(cups)

    # for _ in range(100):
    #     removed_cups = []

    #     # Remove 3 cups after the current cup
    #     for _ in range(3):
    #         removed_cups.append(cups.pop(1))

    #     # Search for destination cup and keep in 1-9
    #     destination_cup = ((cups[0]-2) % size) + 1
    #     while destination_cup in removed_cups:
    #         destination_cup = ((destination_cup-2) % size) + 1
    #     index = cups.index(destination_cup)

    #     # Insert removed cups into cups at pos of dest cup
    #     cups[index+1:index+1] = removed_cups

    #     # Rotate cups as the new current cup is the next one
    #     cups.append(cups.pop(0))

    # Read data
    data = list(map(int, input_data))
    cups = {}

    first_cup = None
    last_cup = None

    for cup_id in data:
        cup = Cup(cup_id)
        cups[cup_id] = cup
        if last_cup:
            last_cup.next_cup = cup
        else:
            first_cup = cup
        last_cup = cup

    # Create a circle of cups
    last_cup.next_cup = first_cup

    size = len(cups)

    current_cup = first_cup

    for _ in range(100):
        removed_cup1 = None

        # Save next cup that is going to be removed
        removed_cup1 = current_cup.next_cup

        # Remove the next three cups from the chain
        current_cup.next_cup = current_cup.next_cup.next_cup.next_cup.next_cup

        # Get destination cup
        removed_cup_ids = [removed_cup1.id, 
                removed_cup1.next_cup.id, 
                removed_cup1.next_cup.next_cup.id]

        dest_cup_id = ((current_cup.id-2) % size) + 1
        while dest_cup_id in removed_cup_ids:
            dest_cup_id = ((dest_cup_id-2) % size) + 1
        dest_cup = cups[dest_cup_id]

        # Append removed cups after the dest_cup
        removed_cup1.next_cup.next_cup.next_cup = dest_cup.next_cup
        dest_cup.next_cup = removed_cup1

        # Select the next cup as the current cup
        current_cup = current_cup.next_cup

    # Create result string based on the cups after cup 1
    cur_cup = cups[1].next_cup
    result = ""
    while cur_cup != cups[1]:
        result += str(cur_cup.id)
        cur_cup = cur_cup.next_cup

    return result


def part2(input_data):
    """
    >>> part2("389125467")
    149245887792
    """

    # Read data
    data = list(map(int, input_data))
    cups = {}

    first_cup = None
    last_cup = None

    for cup_id in data:
        cup = Cup(cup_id)
        cups[cup_id] = cup
        if last_cup:
            last_cup.next_cup = cup
        else:
            first_cup = cup
        last_cup = cup

    # Create all additional cups
    for cup_id in range(max(cups)+1, 1000000+1):
        cup = Cup(cup_id)
        cups[cup_id] = cup
        if last_cup:
            last_cup.next_cup = cup
        last_cup = cup

    # Create a circle of cups
    last_cup.next_cup = first_cup

    size = len(cups)

    current_cup = first_cup

    import tqdm
    for _ in tqdm.tqdm(range(10000000)):
        # Save next cup that is going to be removed
        removed_cup1 = current_cup.next_cup

        # Remove the next three cups from the chain
        current_cup.next_cup = current_cup.next_cup.next_cup.next_cup.next_cup

        # Get destination cup
        removed_cup_ids = [removed_cup1.id, 
                removed_cup1.next_cup.id, 
                removed_cup1.next_cup.next_cup.id]

        dest_cup_id = ((current_cup.id-2) % size) + 1
        while dest_cup_id in removed_cup_ids:
            dest_cup_id = ((dest_cup_id-2) % size) + 1
        dest_cup = cups[dest_cup_id]

        # Append removed cups after the dest_cup
        removed_cup1.next_cup.next_cup.next_cup = dest_cup.next_cup
        dest_cup.next_cup = removed_cup1

        # Select the next cup as the current cup
        current_cup = current_cup.next_cup

    return cups[1].next_cup.id * cups[1].next_cup.next_cup.id


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass