# Advent of Code 2024
# Day 06
# Author: irobin591

import os
import doctest
import copy

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def rotate_dir(dir):
    # up -> right
    if dir == (-1, 0):
        return (0, 1)
    
    # right -> down
    if dir == (0, 1):
        return (1, 0)
    
    # down -> left
    if dir == (1, 0):
        return (0, -1)
    
    # left -> up
    if dir == (0, -1):
        return (-1, 0)

def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    41
    """
    data = []
    for row in input_data:
        row_data = []
        for cell in row:
            row_data.append(cell)
        data.append(row_data)

    cur_x = None
    cur_y = None

    for x, line in enumerate(data):
        for y, cell in enumerate(line):
            if cell == '^':
                cur_x = x
                cur_y = y
                break
        else: 
            continue
        break


    if data[cur_x][cur_y] != '^':
        print('ERROR')
        return
    
    cur_dx = -1
    cur_dy = 0

    spaces = 0

    while cur_x >= 0 and cur_x < len(data) and cur_y >= 0 and cur_y < len(data[0]):
        # Count space and mark cell used
        if data[cur_x][cur_y] != 'X':
            data[cur_x][cur_y] = 'X'
            spaces += 1

        # Check for out of bounds / last space:
        if cur_x + cur_dx < 0 or cur_x + cur_dx >= len(data) or cur_y + cur_dy < 0 or cur_y + cur_dy >= len(data[0]):
            break

        # Check space in front for obstacle
        if data[cur_x + cur_dx][cur_y + cur_dy] == '#':
            # Rotate
            (cur_dx, cur_dy) = rotate_dir((cur_dx, cur_dy))
            continue

        # Move forward
        cur_x += cur_dx
        cur_y += cur_dy
    
    return spaces


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    6
    """
    init_data = []
    for row in input_data:
        row_data = []
        for cell in row:
            row_data.append(cell)
        init_data.append(row_data)

    start_x = None
    start_y = None

    for x, line in enumerate(init_data):
        for y, cell in enumerate(line):
            if cell == '^':
                start_x = x
                start_y = y
                break
        else: 
            continue
        break


    if init_data[start_x][start_y] != '^':
        print('ERROR')
        return
    
    temp_x = start_x
    temp_y = start_y
    temp_dx = -1
    temp_dy = 0

    while temp_x >= 0 and temp_x < len(init_data) and temp_y >= 0 and temp_y < len(init_data[0]):
        # Count space and mark cell used
        if init_data[temp_x][temp_y] != 'X':
            init_data[temp_x][temp_y] = 'X'

        # Check for out of bounds / last space:
        if temp_x + temp_dx < 0 or temp_x + temp_dx >= len(init_data) or temp_y + temp_dy < 0 or temp_y + temp_dy >= len(init_data[0]):
            break

        # Check space in front for obstacle
        if init_data[temp_x + temp_dx][temp_y + temp_dy] == '#':
            # Rotate
            (temp_dx, temp_dy) = rotate_dir((temp_dx, temp_dy))
            continue

        # Move forward
        temp_x += temp_dx
        temp_y += temp_dy
    
    variations = 0
    
    for obs_x, obs_row in enumerate(init_data):
        for obs_y, obs_entry in enumerate(obs_row):
            # print(f"{obs_x} / {obs_y}")
            if init_data[obs_x][obs_y] ==  '^' or init_data[obs_x][obs_y] ==  '#':
                continue

            if init_data[obs_x][obs_y] != 'X':
                continue # 1424
            data = copy.deepcopy(init_data)

            data[obs_x][obs_y] = '#'
    
            cur_x = start_x
            cur_y = start_y

            cur_dx = -1
            cur_dy = 0

            while cur_x >= 0 and cur_x < len(data) and cur_y >= 0 and cur_y < len(data[0]):

                # Check for out of bounds / last space -> obstacle not working
                if cur_x + cur_dx < 0 or cur_x + cur_dx >= len(data) or cur_y + cur_dy < 0 or cur_y + cur_dy >= len(data[0]):
                    break

                # Check space in front for obstacle for wall
                if data[cur_x + cur_dx][cur_y + cur_dy] == '#':
                    # Mark wall as used to check loop
                    data[cur_x + cur_dx][cur_y + cur_dy] = '*'
                    # Rotate and mark obstacle as used
                    (cur_dx, cur_dy) = rotate_dir((cur_dx, cur_dy))
                    continue

                # Check space in front for obstacle for wall
                if data[cur_x + cur_dx][cur_y + cur_dy] == '*':
                    # Mark wall as used to check loop
                    data[cur_x + cur_dx][cur_y + cur_dy] = '+'
                    # Rotate and mark obstacle as used
                    (cur_dx, cur_dy) = rotate_dir((cur_dx, cur_dy))
                    continue

                # Check space in front for obstacle for wall
                if data[cur_x + cur_dx][cur_y + cur_dy] == '+':
                    # Mark wall as used to check loop
                    data[cur_x + cur_dx][cur_y + cur_dy] = '%'
                    # Rotate and mark obstacle as used
                    (cur_dx, cur_dy) = rotate_dir((cur_dx, cur_dy))
                    continue

                # Check space in front for obstacle for wall
                if data[cur_x + cur_dx][cur_y + cur_dy] == '%':
                    # Mark wall as used to check loop
                    data[cur_x + cur_dx][cur_y + cur_dy] = '&'
                    # Rotate and mark obstacle as used
                    (cur_dx, cur_dy) = rotate_dir((cur_dx, cur_dy))
                    continue

                # Check space in front for obstacle for already visited wall
                if data[cur_x + cur_dx][cur_y + cur_dy] == '&':
                    # Abort loop
                    variations += 1
                    break

                # Move forward
                cur_x += cur_dx
                cur_y += cur_dy

    return variations


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass