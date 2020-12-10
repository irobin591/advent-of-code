# Advent of Code 2020
# Day 09
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = [int(x) for x in input_file.read().strip().split('\n')]


class XMASDecoder():
    def __init__(self, data, preamble):
        self.data = data
        self.preamble = preamble

    def get_invalid_numbers(self):
        # iterate though list without preamble and return invalid numbers
        for i in range(self.preamble, len(self.data)):
            preamble = self.data[i-self.preamble:i]
            number = self.data[i]
            if not XMASDecoder.is_valid(preamble, number):
                yield number

    def is_valid(preamble, number):
        # # O(n^2)
        # for num1 in preamble:
        #     for num2 in preamble:
        #         if num1+num2 == number:
        #             return True

        # O(n log n + n)
        preamble.sort() # O(n log n) with quicksort

        left_i = 0
        right_i = len(preamble)-1

        while left_i < right_i: # at most O(n)
            if preamble[left_i] + preamble[right_i] > number:
                right_i -= 1
            elif preamble[left_i] + preamble[right_i] < number:
                left_i += 1
            else:
                return True

        # we have searched all options: number is not a sum of two numbers in preamble
        return False

    def find_encryption_weakness(self, invalid_number):
        for i_number, number in enumerate(self.data):
            if number > invalid_number:
                continue

            sum_of_numbers = number
            min_number = number
            max_number = number
            # print(number)

            # Check the following numbers
            for number2 in self.data[i_number+1:]:
                # print("  {}".format(number2))
                sum_of_numbers += number2

                # if we overshoot the target: break out of the loop
                if sum_of_numbers > invalid_number:
                    break

                # Calc min and max numbers:
                min_number = min(min_number, number2)
                max_number = max(max_number, number2)

                # if we hit the target number: return the sum of the smallest and the largest number
                if sum_of_numbers == invalid_number:
                    return min_number + max_number

            

def part1(input_data, preamble=25):
    """
    >>> part1([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576], preamble=5)
    127
    """
    decoder = XMASDecoder(input_data, preamble=preamble)
    return next(decoder.get_invalid_numbers())


def part2(input_data, preamble=25):
    """
    >>> part2([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576], preamble=5)
    62
    """
    decoder = XMASDecoder(input_data, preamble=preamble)
    invalid_number = next(decoder.get_invalid_numbers())
    return decoder.find_encryption_weakness(invalid_number)


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass