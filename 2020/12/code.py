# Advent of Code 2020
# Day 12
# Author: irobin591

import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


class Ship():
    def __init__(self, start_pos_north=0, start_pos_east=0, start_dir_north=0, start_dir_east=1):
        self.pos_north = start_pos_north
        self.pos_east  = start_pos_east
        self.dir_north = start_dir_north
        self.dir_east  = start_dir_east

    @property
    def distance(self):
        return abs(self.pos_north) + abs(self.pos_east)

    def rotate(self, direction, degree):
        if (direction == 'L' and degree == 90) or (direction == 'R' and degree == 270):
            # Rotate 90° counter-clockwise
            new_dir_north =  1 * self.dir_east
            new_dir_east  = -1 * self.dir_north
        elif (direction == 'L' and degree == 180) or (direction == 'R' and degree == 180):
            # Rotate 180° counter-clockwise
            new_dir_north = -1 * self.dir_north
            new_dir_east  = -1 * self.dir_east
        elif (direction == 'L' and degree == 270) or (direction == 'R' and degree == 90):
            # Rotate 180° counter-clockwise
            new_dir_north = -1 * self.dir_east
            new_dir_east  =  1 * self.dir_north
        else:
            raise RuntimeError("Invalid direction/degree for rotation")

        # Update rotations
        self.dir_east = new_dir_east
        self.dir_north = new_dir_north

    def move(self, direction, amount):
        if direction == 'N':
            # Move north
            self.pos_north += amount
        elif direction == 'S':
            # Move south
            self.pos_north -= amount
        elif direction == 'E':
            # Move east
            self.pos_east += amount
        elif direction == 'W':
            # Move west
            self.pos_east -= amount
        else:
            raise RuntimeError("Invalid direction for movement")

    def change_dir(self, direction, amount):
        if direction == 'N':
            # Move waypoint north
            self.dir_north += amount
        elif direction == 'S':
            # Move waypoint south
            self.dir_north -= amount
        elif direction == 'E':
            # Move waypoint east
            self.dir_east += amount
        elif direction == 'W':
            # Move waypoint west
            self.dir_east -= amount
        else:
            raise RuntimeError("Invalid direction for movement")

    def forward(self, amount):
        self.pos_north += self.dir_north * amount
        self.pos_east  += self.dir_east * amount


def test_ship():
    test_ship_part1()
    test_ship_part2()


def test_ship_part1():
    ship = Ship(0, 0, 0, 1)
    assert ship.pos_east == 0, "Wrong initial start position"
    assert ship.pos_north == 0, "Wrong initial start position"
    assert ship.dir_east == 1, "Wrong initial start rotation"
    assert ship.dir_north == 0, "Wrong initial start rotation"

    # F10
    ship.forward(10)

    assert ship.pos_east == 10, "Wrong updated position"
    assert ship.pos_north == 0, "Wrong updated position"
    assert ship.dir_east == 1, "Wrong updated rotation"
    assert ship.dir_north == 0, "Wrong updated rotation"

    # N3
    ship.move('N', 3)

    assert ship.pos_east == 10, "Wrong updated position"
    assert ship.pos_north == 3, "Wrong updated position"
    assert ship.dir_east == 1, "Wrong updated rotation"
    assert ship.dir_north == 0, "Wrong updated rotation"

    # F7
    ship.forward(7)

    assert ship.pos_east == 17, "Wrong updated position"
    assert ship.pos_north == 3, "Wrong updated position"
    assert ship.dir_east == 1, "Wrong updated rotation"
    assert ship.dir_north == 0, "Wrong updated rotation"

    # R90
    ship.rotate('R', 90)

    assert ship.pos_east == 17, "Wrong updated position"
    assert ship.pos_north == 3, "Wrong updated position"
    assert ship.dir_east == 0, "Wrong updated rotation"
    assert ship.dir_north == -1, "Wrong updated rotation"

    # F11
    ship.forward(11)

    assert ship.pos_east == 17, "Wrong updated position"
    assert ship.pos_north == -8, "Wrong updated position"
    assert ship.dir_east == 0, "Wrong updated rotation"
    assert ship.dir_north == -1, "Wrong updated rotation"

    assert ship.distance == 25, "Wrong distance calculated"

    
def test_ship_part2():
    ship = Ship(0, 0, 1, 10)

    assert ship.pos_east == 0, "Wrong initial start position"
    assert ship.pos_north == 0, "Wrong initial start position"
    assert ship.dir_east == 10, "Wrong initial start rotation"
    assert ship.dir_north == 1, "Wrong initial start rotation"

    # F10
    ship.forward(10)

    assert ship.pos_east == 100, "Wrong updated position"
    assert ship.pos_north == 10, "Wrong updated position"
    assert ship.dir_east == 10, "Wrong updated rotation"
    assert ship.dir_north == 1, "Wrong updated rotation"

    # N3
    ship.change_dir('N', 3)

    assert ship.pos_east == 100, "Wrong updated position"
    assert ship.pos_north == 10, "Wrong updated position"
    assert ship.dir_east == 10, "Wrong updated rotation"
    assert ship.dir_north == 4, "Wrong updated rotation"

    # F7
    ship.forward(7)

    assert ship.pos_east == 170, "Wrong updated position"
    assert ship.pos_north == 38, "Wrong updated position"
    assert ship.dir_east == 10, "Wrong updated rotation"
    assert ship.dir_north == 4, "Wrong updated rotation"

    # R90
    ship.rotate('R', 90)

    assert ship.pos_east == 170, "Wrong updated position"
    assert ship.pos_north == 38, "Wrong updated position"
    assert ship.dir_east == 4, "Wrong updated rotation"
    assert ship.dir_north == -10, "Wrong updated rotation"

    # F11
    ship.forward(11)

    assert ship.pos_east == 214, "Wrong updated position"
    assert ship.pos_north == -72, "Wrong updated position"
    assert ship.dir_east == 4, "Wrong updated rotation"
    assert ship.dir_north == -10, "Wrong updated rotation"

    assert ship.distance == 286, "Wrong distance calculated"


def part1(input_data):
    ship = Ship(0, 0, 0, 1)

    for line in input_data:
        action = line[0]
        amount = int(line[1:])

        if action in ['N', 'S', 'E', 'W']:
            ship.move(action, amount)
        elif action in ['L', 'R']:
            ship.rotate(action, amount)
        elif action == 'F':
            ship.forward(amount)
        else:
            raise RuntimeError("Unknown action")

    return ship.distance


def part2(input_data):
    ship = Ship(0, 0, 1, 10)

    for line in input_data:
        action = line[0]
        amount = int(line[1:])

        if action in ['N', 'S', 'E', 'W']:
            ship.change_dir(action, amount)
        elif action in ['L', 'R']:
            ship.rotate(action, amount)
        elif action == 'F':
            ship.forward(amount)
        else:
            raise RuntimeError("Unknown action")

    return ship.distance


if __name__ == "__main__":
    test_ship()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass