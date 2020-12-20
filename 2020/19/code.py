# Advent of Code 2020
# Day 19
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

# Prep Input
# input_data = list(map(int, input_data.strip().split('\n')))

re_rule_int = re.compile(r'^(\d+): ([\d |]+)$')
re_rule_char = re.compile(r'^(\d+): "([a-z])"$')
re_rule_input = re.compile(r'^([ab]+)$')


def check_rule(string, rule_to_check, ruleset):
    # end of string and still a rule to check: no success (and no str to return)
    if len(string) == 0:
        return

    # if rule is a char rule, compare the first char and return the rest as remaining
    if type(rule_to_check) == str:
        if rule_to_check == string[0]:
            yield string[1:]
        return 

    # for each or (x | x) rule:
    for rules in rule_to_check:
        # start with input string as valid remaining string
        remaining_strings = [string]
        valid = True

        # check all remaining strings for each sequential rule
        for rule in rules:
            remaining_strings_next = []
            for remaining_string in remaining_strings:
                results = check_rule(remaining_string, ruleset[rule], ruleset)

                tmp = list(results)

                remaining_strings_next.extend(tmp)
            remaining_strings = remaining_strings_next
        
        # if a remaining string is available: yield all
        if len(remaining_strings):
            yield from remaining_strings

def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    2
    """
    rules = {} 
    count_valid_inputs = 0
    for line in input_data:
        # Regex for combined rule
        r_rule_int = re_rule_int.match(line)
        if r_rule_int:
            # Add rule int:
            rule_id, rule_set = r_rule_int.groups()
            rules[int(rule_id)] = [list(map(int, x.split(' '))) for x in rule_set.split(' | ')]
            continue

        # Regex for final rules (resulting in a character)
        r_rule_char = re_rule_char.match(line)
        if r_rule_char:
            # Add rule int:
            rule_id, rule_char = r_rule_char.groups()
            rules[int(rule_id)] = str(rule_char)
            continue
        
        # Regex for test input (rules have to be progressed first)
        r_rule_input = re_rule_input.match(line)
        if r_rule_input:
            remaining_strings = list(check_rule(r_rule_input.group(1), rules[0], rules))
            if "" in remaining_strings:
                count_valid_inputs += 1
            continue

    return count_valid_inputs

def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part2.txt"), 'r').read().strip().split('\\n'))
    12
    """
    rules = {} 
    count_valid_inputs = 0
    for line in input_data:
        # Regex for combined rule
        r_rule_int = re_rule_int.match(line)
        if r_rule_int:
            # Add rule int:
            rule_id, rule_set = r_rule_int.groups()

            # OVERRIDE RULES 8 AND 11
            if rule_id == '8':
                rule_set = "42 | 42 8"
            if rule_id == '11':
                rule_set = "42 31 | 42 11 31"
            
            rules[int(rule_id)] = [list(map(int, x.split(' '))) for x in rule_set.split(' | ')]
            continue

        # Regex for final rules (resulting in a character)
        r_rule_char = re_rule_char.match(line)
        if r_rule_char:
            # Add rule int:
            rule_id, rule_char = r_rule_char.groups()
            rules[int(rule_id)] = str(rule_char)
            continue
        
        # Regex for test input (rules have to be progressed first)
        r_rule_input = re_rule_input.match(line)
        if r_rule_input:
            # Output all possible remaining strings
            remaining_strings = list(check_rule(r_rule_input.group(1), rules[0], rules))
            # Check if "" is a remaining string 
            # (this means that everything has been successfully parsed
            #   and nothing remained afterwards)
            if "" in remaining_strings:
                count_valid_inputs += 1
            continue

    return count_valid_inputs


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass