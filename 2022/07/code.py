# Advent of Code 2022
# Day 07
# Author: irobin591

import os
import doctest
import directory

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    95437
    """

    root = directory.Directory()
    all_dirs = [ root ]
    current_path = None

    for line in input_data:
        if line.startswith('$ '):
            cmd = line[2:]

            if cmd == 'cd /':
                current_path = root
                continue

            if cmd.startswith('cd '):
                current_path = current_path.chdir(cmd[3:])
                continue

            continue
        
        if line.startswith('dir '):
            new_dir = current_path.add_dir(line[4:])
            all_dirs.append(new_dir)
            continue

        file_size, file_name = line.split(' ')

        current_path.add_file(file_name, int(file_size))

    total_sizes = 0

    for available_dir in all_dirs:
        size = available_dir.total_size()

        if size < 100000:
            total_sizes += size

    return total_sizes


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test.txt"), 'r').read().strip().split('\\n'))
    24933642
    """
    root = directory.Directory()
    all_dirs = [ root ]
    current_path = None

    for line in input_data:
        if line.startswith('$ '):
            cmd = line[2:]

            if cmd == 'cd /':
                current_path = root
                continue

            if cmd.startswith('cd '):
                current_path = current_path.chdir(cmd[3:])
                continue

            continue
        
        if line.startswith('dir '):
            new_dir = current_path.add_dir(line[4:])
            all_dirs.append(new_dir)
            continue

        file_size, file_name = line.split(' ')

        current_path.add_file(file_name, int(file_size))

    disk_size = 70000000
    # minimum amount of size to free
    threshold = 30000000 - (disk_size - root.total_size())

    smallest_dir_to_delete = root.total_size()

    for available_dir in all_dirs:
        size = available_dir.total_size()

        if size > threshold and size < smallest_dir_to_delete:
            smallest_dir_to_delete = size

    return smallest_dir_to_delete


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass