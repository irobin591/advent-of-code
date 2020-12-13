# Advent of Code 2020
# Day 13
# Author: irobin591

import os
import doctest
import math

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(["939","7,13,x,x,59,x,31,19"])
    295
    """
    timestamp = int(input_data[0])
    bus_ids = input_data[1].split(',')
    # Ignore bus_ids with 'x'
    bus_ids = map(int, filter(lambda bus_id: bus_id != 'x', bus_ids))
    # (id, time_to_wait)
    # last_busstop = timestamp % id
    # time_to_wait = id - last_busstop
    bus_ids = [(bus_id, bus_id - (timestamp % bus_id)) for bus_id in bus_ids]

    bus_ids.sort(key=lambda x: x[1])

    next_bus_id, next_bus_time_to_wait = bus_ids[0]

    return next_bus_id * next_bus_time_to_wait

# https://stackoverflow.com/a/51716959
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def part2(input_data):
    """
    >>> part2(["939","7,13,x,x,59,x,31,19"])
    1068781
    >>> part2(["0","17,x,13,19"])
    3417
    >>> part2(["0","67,7,59,61"])
    754018
    >>> part2(["0","67,x,7,59,61"])
    779210
    >>> part2(["0","67,7,x,59,61"])
    1261476
    >>> part2(["0","1789,37,47,1889"])
    1202161486
    """
    bus_ids = input_data[1].split(',')
    
    # covert numbers to ints
    bus_ids = [int(bus_id) if bus_id != 'x' else None for bus_id in bus_ids]

    # (bus_id, needed_modulo_on_timestamp)
    bus_timestamp = [(bus_id, -i % bus_id) if bus_id else None for i,bus_id in enumerate(bus_ids)]
    # Ignore 'x'
    bus_timestamp = list(filter(lambda x: x, bus_timestamp))

    # Start with 0
    cur_timestamp = 0
    # Increase by lcm, starting with the initial value
    # keeps cur_timestamp % first_value = 0
    cur_lcm = bus_timestamp[0][0]
    # Remove first from list
    bus_timestamp.pop(0)

    # while list of busses
    while len(bus_timestamp):
        # Increase by lcm to keep already reached modulos
        cur_timestamp += cur_lcm
        # if the result of the modulo of a bus is correct, calculate new lcm 
        # and remove from list
        # -> keep this modulo because we add a multiplier of the bus_id
        # 15 % 4 = 3 
        # 15+(4*x) % 4 = 3 with x being an integer
        if cur_timestamp % bus_timestamp[0][0] == bus_timestamp[0][1]:
            cur_lcm = lcm(cur_lcm, bus_timestamp[0][0])
            bus_timestamp.pop(0)

    return cur_timestamp


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass