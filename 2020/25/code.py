# Advent of Code 2020
# Day 25
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = list(map(int, input_file.read().strip().split('\n')))


def part1(input_data):
    """
    >>> part1([5764801, 17807724])
    14897079
    """
    card_pubkey = input_data[0]
    door_pubkey = input_data[1]

    N = 20201227

    # crack the RSA:
    base = 7
    e = 0
    cur = 1

    # Step 1: Calc the loop size e for either the card or the door, whichever is smaller
    while cur != card_pubkey and cur != door_pubkey:
        cur = base * cur % N
        e += 1

    if cur == card_pubkey:
        cur = door_pubkey
    elif cur == door_pubkey:
        cur = card_pubkey
    else:
        raise RuntimeError("")

    # Step 2: calc and return the encryption key
    return pow(cur, e, N)


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    pass