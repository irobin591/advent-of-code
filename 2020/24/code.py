# Advent of Code 2020
# Day 24
# Author: irobin591

import os
import doctest
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def parse_tile(tile_string):
    """
    >>> parse_tile("esew")
    (1, -1)
    >>> parse_tile("esewnw")
    (0, 0)
    >>> parse_tile("nwwswee")
    (0, 0)
    """
    data = list(tile_string)
    cur_pos_ew = 0
    cur_pos_ns = 0
    while len(data) != 0:
        c1 = data.pop(0)
        if c1 == 'w':
            cur_pos_ew -= 1
        elif c1 == 'e':
            cur_pos_ew += 1
        elif c1 == 's':
            c2 = data.pop(0)
            cur_pos_ns -= 1
            if c2 == 'e':
                cur_pos_ew += 1
            pass
        elif c1 == 'n':
            c2 = data.pop(0)
            cur_pos_ns += 1
            if c2 == 'w':
                cur_pos_ew -= 1
            pass
        else:
            raise RuntimeError("")
    return cur_pos_ew, cur_pos_ns


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    10
    """
    # index: (e/w, n/s)
    tiles = defaultdict(lambda: 0)

    for line in input_data:
        pos = parse_tile(line)
        tiles[pos] += 1
        x = 1

    return sum(map(lambda x: x % 2 == 1, tiles.values()))


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    2208
    """
    tiles = defaultdict(lambda: 0)
    directions = list(map(parse_tile, ["e", "se", "ne", "w", "sw", "nw"]))

    for line in input_data:
        pos = parse_tile(line)
        tiles[pos] += 1
        x = 1

    for day in range(100):
        count_neighbors = defaultdict(lambda: 0)

        for tile in tiles:
            if tiles[tile] % 2 == 1:
                # tile is black
                for neighbor in directions:
                    new_pos = (tile[0] + neighbor[0], tile[1] + neighbor[1])
                    count_neighbors[new_pos] += 1

        new_tiles = tiles.copy()
        
        # Check black tiles
        for tile in tiles:
            if tiles[tile] % 2 == 1:
                # tile is black
                if count_neighbors[tile] == 0 or count_neighbors[tile] > 2:
                    # zero or more than 2 tiles:
                    #   flip to white
                    new_tiles[tile] = 0

        # Check white tiles
        for tile in count_neighbors:
            if tiles[tile] % 2 == 0:
                # tile is white
                if count_neighbors[tile] == 2:
                    # two black neighbors: flip to black
                    new_tiles[tile] = 1

        tiles = new_tiles



    return sum(map(lambda x: x % 2 == 1, tiles.values()))


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass