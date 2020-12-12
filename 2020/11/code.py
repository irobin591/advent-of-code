# Advent of Code 2020
# Day 11
# Author: irobin591

import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


class AirportSeatPlan():
    EMPTY = 'L'
    OCCUPIED = '#'
    FLOOR = '.'

    def __init__(self, data_map):
        self.data_map = [list(x) for x in data_map]
        self.size_h = len(data_map)
        self.size_v = len(data_map[0])

    def get_seats(self, seat_type=OCCUPIED):
        count = sum([
            sum(map(lambda x: x == seat_type, line)) 
            for line in self.data_map
            ])
        return count

    def count_neighbor_seats(obj, h, v):
        occupied_seats = 0
        # Check neighbors
        for neighbor_h in [h-1, h, h+1]:
            # Check if neighbor_x is in bounds
            if neighbor_h < 0 or neighbor_h >= len(obj.data_map):
                continue

            neighbor_h_line = obj.data_map[neighbor_h]
            for neighbor_v in [v-1, v, v+1]:
                # Check if neighbor_y is in bounds
                if neighbor_v < 0 or neighbor_v >= len(neighbor_h_line):
                    continue
                
                # Skip item itself
                if neighbor_h == h and neighbor_v == v:
                    continue

                if neighbor_h_line[neighbor_v] == AirportSeatPlan.OCCUPIED:
                    occupied_seats += 1
        return occupied_seats

    def count_sight_seats(obj, h, v):
        occupied_seats = 0
        # Check neighbors
        for sight_h in [-1, 0, +1]:
            for sight_v in [-1, 0, +1]:
                # Skip no movement
                if sight_h == 0 and sight_v == 0:
                    continue

                cur_pos_h = h + sight_h
                cur_pos_v = v + sight_v

                # Repeat while position is in bounds
                while (cur_pos_h >= 0 and cur_pos_h < obj.size_h and 
                        cur_pos_v >= 0 and cur_pos_v < obj.size_v):

                    # Check if place is a seat or not
                    place = obj.data_map[cur_pos_h][cur_pos_v]
                    if place == AirportSeatPlan.EMPTY:
                        break
                    if place == AirportSeatPlan.OCCUPIED:
                        occupied_seats += 1
                        break

                    # Go one step further if place is not a seat
                    cur_pos_h += sight_h
                    cur_pos_v += sight_v
        return occupied_seats
    
    def iterate(self, tolerance, func_neighbor_eval):
        updated_data_map = []
        for h, h_line in enumerate(self.data_map):
            updated_data_map.append([])
            for v in range(len(h_line)):
                occupied_neighbor_seats = func_neighbor_eval(self, h, v)
                new_char = self.data_map[h][v]
                if new_char != AirportSeatPlan.FLOOR and occupied_neighbor_seats == 0:
                    new_char = AirportSeatPlan.OCCUPIED
                if new_char != AirportSeatPlan.FLOOR and occupied_neighbor_seats >= tolerance:
                    new_char = AirportSeatPlan.EMPTY
                updated_data_map[h].append(new_char)
        return AirportSeatPlan(updated_data_map)
    
    def full_iterations(self, tolerance, func_neighbor_eval):
        t = self
        while True:
            # Run an iteration
            t_next = t.iterate(tolerance, func_neighbor_eval)

            # Check if the iteration changed the map
            if t == t_next:
                # Return current map
                return t_next

            t = t_next

    def __str__(self):
        return "\n".join(["".join(x) for x in self.data_map])

    def __eq__(self, other):
        return self.data_map == other.data_map


def test():
    test_map = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
    t = AirportSeatPlan(test_map)
    
    t_end = t.full_iterations(4, AirportSeatPlan.count_neighbor_seats)
    assert t_end.get_seats() == 37, "Seat calculation for Part 1 is wrong"

    t_end = t.full_iterations(5, AirportSeatPlan.count_sight_seats)
    assert t_end.get_seats() == 26, "Seat calculation for Part 2 is wrong"


def part1(input_data):
    t = AirportSeatPlan(input_data)
    
    t_end = t.full_iterations(4, AirportSeatPlan.count_neighbor_seats)
    return t_end.get_seats()


def part2(input_data):
    t = AirportSeatPlan(input_data)
    
    t_end = t.full_iterations(5, AirportSeatPlan.count_sight_seats)
    return t_end.get_seats()


if __name__ == "__main__":
    test()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass