from math import floor
import doctest

def part1(input_data):
    """
    >>> part1([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]
    >>> part1([2,3,0,3,99])
    [2, 3, 0, 6, 99]
    >>> part1([2,4,4,5,99,0])
    [2, 4, 4, 5, 99, 9801]
    >>> part1([1,1,1,4,99,5,6,0,99])
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    """

    cur = 0

    while cur < len(input_data):
        opcode = input_data[cur]
        # print("{}: {}".format(cur, opcode))
        if opcode == 1:
            input_data[input_data[cur+3]] = input_data[input_data[cur+1]] + input_data[input_data[cur+2]]
            cur += 4
            
        if opcode == 2:
            input_data[input_data[cur+3]] = input_data[input_data[cur+1]] * input_data[input_data[cur+2]]
            cur += 4

        if opcode == 99:
            return input_data


    return input_data


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        for line in infile:
            input_data = list(map(int, line.split(',')))
            input_data[1] = 12
            input_data[2] = 2
            print(part1(input_data))
