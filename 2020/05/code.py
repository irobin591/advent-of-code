# Advent of Code 2020
# Day 05
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


class Seat():
    def __init__(self, seat_code):
        self.seat_code = seat_code
        self.row = int(seat_code[:7].replace('F', '0').replace('B', '1'), 2)
        self.column = int(seat_code[-3:].replace('L', '0').replace('R', '1'), 2)
        self.seat_id = self.row * 8 + self.column


def part1(input_data):
    """
    >>> part1(["FBFBBFFRLR"])
    357
    >>> part1(["BFFFBBFRRR"])
    567
    >>> part1(["FFFBBBFRRR"])
    119
    >>> part1(["BBFFBBFRLL"])
    820
    """
    return max([Seat(l).seat_id for l in input_data])


def part2(input_data):
    used_seats = [Seat(l).seat_id for l in input_data]
    for seat in range(1024):
        if seat not in used_seats:
            if seat+1 in used_seats and seat-1 in used_seats:
                return seat
    return -1


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass