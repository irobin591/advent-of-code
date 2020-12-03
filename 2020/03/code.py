# Advent of Code 2020
# Day 03
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def prep_data(input_data):
    class Repeat():
        def __init__(self, array):
            self._array = array
            self._length = len(array)
        def __iter__(self):
            self._cur = 0
            return self
        def __next__(self):
            x = self._array[self._cur]
            self._cur = (self._cur + 1) % self._length
            return x
        def __getitem__(self, key): 
            return self._array[int(key) % self._length]
    return list(map(Repeat, input_data))

def check_slope(data, h_step: int, v_step: int):
    h = 0
    v = 0
    count = 0
    while True:
        if h >= len(data):
            return count
        c = data[h][v]
        if c == '#':
            count += 1
        h += h_step
        v += v_step


def part1(input_data):
    """
    >>> part1(["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"])
    7
    """
    data = prep_data(input_data)
    return check_slope(data, 1, 3)

def part2(input_data):
    """
    >>> part2(["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"])
    336
    """
    data = prep_data(input_data)
    slope1 = check_slope(data, 1, 1)
    slope2 = check_slope(data, 1, 3)
    slope3 = check_slope(data, 1, 5)
    slope4 = check_slope(data, 1, 7)
    slope5 = check_slope(data, 2, 1)
    return slope1 * slope2 * slope3 * slope4 * slope5


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass