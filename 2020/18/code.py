# Advent of Code 2020
# Day 18
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def calc1(symbols):
    cur_result = 0
    next_op = "+"
    while len(symbols) != 0:
        symbol = symbols.pop(0)
        if symbol == '+':
            next_op = "+"
        elif symbol == '*':
            next_op = "*"
        elif symbol.startswith('(') and symbol != '(':
            symbols.insert(0, symbol[1:])
            symbols.insert(0, symbol[0])
        elif symbol.endswith(')') and symbol != ')':
            symbols.insert(0, symbol[-1])
            symbols.insert(0, symbol[:-1])
        elif symbol == '(':
            result = calc1(symbols)
            symbols.insert(0, str(result))
        elif symbol == ')':
            break
        else:
            if next_op == '+':
                cur_result += int(symbol)
            elif next_op == '*':
                cur_result *= int(symbol)
            else:
                raise RuntimeError()

    return cur_result


def calc2(symbols):
    cur_mult = 1
    cur_sum = 0
    while len(symbols) != 0:
        symbol = symbols.pop(0)
        if symbol == '+':
            pass
        elif symbol == '*':
            cur_mult *= cur_sum
            cur_sum = 0
        elif symbol.startswith('(') and symbol != '(':
            symbols.insert(0, symbol[1:])
            symbols.insert(0, symbol[0])
        elif symbol.endswith(')') and symbol != ')':
            symbols.insert(0, symbol[-1])
            symbols.insert(0, symbol[:-1])
        elif symbol == '(':
            result = calc2(symbols)
            symbols.insert(0, str(result))
        elif symbol == ')':
            break
        else:
            cur_sum += int(symbol)

    if cur_sum != 0:
        cur_mult *= cur_sum
    return cur_mult


def part1(input_data):
    """
    >>> part1(["2 * 3 + (4 * 5)"])
    26
    >>> part1(["5 + (8 * 3 + 9 + 3 * 4 * 3)"])
    437
    >>> part1(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"])
    12240
    >>> part1(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"])
    13632
    """
    result = 0

    for line in input_data:
        result += calc1(line.split(' '))

    return result


def part2(input_data):
    """
    >>> part2(["1 + 2 * 3 + 4 * 5 + 6"])
    231
    >>> part2(["1 + (2 * 3) + (4 * (5 + 6))"])
    51
    >>> part2(["2 * 3 + (4 * 5)"])
    46
    >>> part2(["5 + (8 * 3 + 9 + 3 * 4 * 3)"])
    1445
    >>> part2(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"])
    669060
    >>> part2(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"])
    23340
    """
    result = 0

    for line in input_data:
        result += calc2(line.split(' '))

    return result


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass