# Advent of Code 2020
# Day 17
# Author: irobin591

import os
import doctest
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

class ConwayCube():
    def from_input(input_data):
        initial_cubes = []
        for x, line in enumerate(input_data):
            for y, cube in enumerate(line):
                if cube == '#':
                    initial_cubes.append((x,y,0))
        return ConwayCube(initial_cubes)

    def __init__(self, initial_cubes):
        self.active_cubes = initial_cubes # (0, 0, 0)
        self.iteration = 0
    
    def iterate(self):
        neighbor_cubes = []
        for cube in self.active_cubes:
            # add all 26 neighbors to neighbor_cubes
            for x_diff in [-1, 0, 1]:
                for y_diff in [-1, 0, 1]:
                    for z_diff in [-1, 0, 1]:
                        if x_diff == 0 and y_diff == 0 and z_diff == 0:
                            continue
                        neighbor_cubes.append((cube[0]+x_diff, cube[1]+y_diff, cube[2]+z_diff))


        # count the cells in neighbor_cubes
        counter_neighbors = Counter(neighbor_cubes)
        x = 1

        # for each cube either active or in the neighbor set: check the rules
        for cube in set(list(counter_neighbors.keys()) + self.active_cubes):
            if cube in self.active_cubes:
                if cube not in counter_neighbors or counter_neighbors[cube] < 2 or counter_neighbors[cube] > 3:
                    self.active_cubes.remove(cube)
            else:
                if cube in counter_neighbors and counter_neighbors[cube] == 3:
                    self.active_cubes.append(cube)
        
        self.iteration += 1


class ConwayHyperCube():
    def from_input(input_data):
        initial_cubes = []
        for x, line in enumerate(input_data):
            for y, cube in enumerate(line):
                if cube == '#':
                    initial_cubes.append((x, y, 0, 0))
        return ConwayHyperCube(initial_cubes)

    def __init__(self, initial_cubes):
        self.active_cubes = initial_cubes # (0, 0, 0, 0)
        self.iteration = 0
    
    def iterate(self):
        neighbor_cubes = []
        for cube in self.active_cubes:
            # add all 80 neighbors to neighbor_cubes
            for x_diff in [-1, 0, 1]:
                for y_diff in [-1, 0, 1]:
                    for z_diff in [-1, 0, 1]:
                        for w_diff in [-1, 0, 1]:
                            if x_diff == 0 and y_diff == 0 and z_diff == 0 and w_diff == 0:
                                continue
                            neighbor_cubes.append((cube[0]+x_diff, cube[1]+y_diff, cube[2]+z_diff, cube[3]+w_diff))


        # count the cells in neighbor_cubes
        counter_neighbors = Counter(neighbor_cubes)
        x = 1

        # for each cube either active or in the neighbor set: check the rules
        for cube in set(list(counter_neighbors.keys()) + self.active_cubes):
            if cube in self.active_cubes:
                if cube not in counter_neighbors or counter_neighbors[cube] < 2 or counter_neighbors[cube] > 3:
                    self.active_cubes.remove(cube)
            else:
                if cube in counter_neighbors and counter_neighbors[cube] == 3:
                    self.active_cubes.append(cube)
        
        self.iteration += 1


def part1(input_data):
    """
    >>> part1([".#.","..#","###"])
    112
    """
    cube = ConwayCube.from_input(input_data)
    for _ in range(6):
        cube.iterate()

    return len(cube.active_cubes)


def part2(input_data):
    """
    >>> part2([".#.","..#","###"])
    848
    """
    cube = ConwayHyperCube.from_input(input_data)
    for _ in range(6):
        cube.iterate()

    return len(cube.active_cubes)


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass