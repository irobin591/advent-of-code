# Advent of Code 2024
# Day 02
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def safe_report(report):
    last_no = report[0]
    cur_no = report[1]

    cur_index = 1

    increasing = cur_no > last_no

    while True:
        if cur_no == last_no:
            return False

        if (cur_no > last_no) != increasing:
            return False

        if abs(cur_no - last_no) > 3:
            return False

        if cur_index + 1 == len(report):
            return True

        cur_index += 1

        last_no = cur_no
        cur_no = report[cur_index]


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    2
    """

    data = []

    for line in input_data:
        data.append(list(map(lambda x : int(x), line.split(' '))))

    safe_reports = 0

    for entry in data:
        safe_reports += 1 if safe_report(entry) else 0

    return safe_reports


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    4
    >>> part2(["1 3 2 4 5"])
    1
    >>> part2(["1 4 3 4 5"])
    1
    >>> part2(["1 2 3 4 5"])
    1
    >>> part2(["3 2 3 4 5"])
    1
    """
    data = []

    for line in input_data:
        data.append(list(map(lambda x : int(x), line.split(' '))))

    safe_reports = 0

    for entry in data:
        if safe_report(entry):
            safe_reports += 1
        else:
            for i in range(len(entry)):
                temp_report = entry.copy()
                temp_report.pop(i)

                if safe_report(temp_report):
                    safe_reports += 1
                    break

    return safe_reports


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass