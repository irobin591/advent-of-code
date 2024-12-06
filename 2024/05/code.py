# Advent of Code 2024
# Day 05
# Author: irobin591

import os
import doctest


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as input_file:
        input_data = input_file.read().strip()
    return input_data


def part1(input_data):
    """
    >>> part1(read_file("test_part1.txt"))
    143
    """

    rulesdata, testdata = input_data.split('\n\n')
    rulesdata = rulesdata.split('\n')
    testdata = testdata.split('\n')

    rules = {}

    for ruledata in rulesdata:
        rule_pre, rule_post = ruledata.split('|')
        rule_pre = int(rule_pre)
        rule_post = int(rule_post)

        if rule_pre not in rules:
            rules[rule_pre] = []
        
        rules[rule_pre].append(rule_post)

    target = 0

    for row in testdata:
        test = list(map(lambda x: int(x), row.split(',')))

        abort = False
        mid_number = 0

        j = 1

        while j < len(test):
            for i in range(j):
                if test[j] in rules and test[i] in rules[test[j]]:
                    abort = True
                    break
            
            if abort:
                break

            j += 1

        if not abort:
            target += test[len(test) // 2]

    return target


def part2(input_data):
    """
    >>> part2(read_file("test_part1.txt"))
    123
    """
    rulesdata, testdata = input_data.split('\n\n')
    rulesdata = rulesdata.split('\n')
    testdata = testdata.split('\n')
    print(rulesdata)

    rules = {}

    for ruledata in rulesdata:
        rule_pre, rule_post = ruledata.split('|')
        rule_pre = int(rule_pre)
        rule_post = int(rule_post)

        if rule_pre not in rules:
            rules[rule_pre] = []
        
        rules[rule_pre].append(rule_post)

    print(rules)

    target = 0

    for row in testdata:
        test = list(map(lambda x: int(x), row.split(',')))

        abort = False
        mid_number = 0

        j = 1

        while j < len(test):
            for i in range(j):
                if test[j] in rules and test[i] in rules[test[j]]:
                    abort = True
                    break
            
            if abort:
                break

            j += 1

        if not abort:
            continue

        print(test)

        j = 1

        success = False

        while not success:
            success = True
            while j < len(test):
                data_post = test[j]
                for i in range(j):
                    data_pre = test[i]
                    if test[j] in rules and test[i] in rules[test[j]]:
                        test[i] = data_post
                        test[j] = data_pre
                        success = False
                        break
                
                if not success:
                    break

                j += 1

        
        target += test[len(test) // 2]

    return target


if __name__ == "__main__":
    doctest.testmod()
    input_data = read_file('input.txt')
    # print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass