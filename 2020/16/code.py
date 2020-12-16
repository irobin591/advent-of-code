# Advent of Code 2020
# Day 16
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

regex_field_rule = re.compile(r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

def part1(input_data):
    """
    >>> part1(["class: 1-3 or 5-7","row: 6-11 or 33-44","seat: 13-40 or 45-50","","your ticket:","7,1,14","","nearby tickets:","7,3,47","40,4,50","55,2,20","38,6,12"])
    71
    """
    # print(input_data)
    stage = 0
    valid_fields = []
    error_rate = 0
    for line in input_data:
        r_field_rule = regex_field_rule.match(line)
        if r_field_rule:
            # print(line)
            # print(r_field_rule.groups())
            valid_fields.append({
                "name": r_field_rule.group(1),
                "ranges": [
                    range(int(r_field_rule.group(2)), int(r_field_rule.group(3))+1),
                    range(int(r_field_rule.group(4)), int(r_field_rule.group(5))+1),
                ]
            })
            pass
        elif line.strip() == "your ticket:":
            stage = 1
        elif line.strip() == "nearby tickets:":
            stage = 2
        else:
            if stage == 1:
                # your ticket
                pass
            elif stage == 2:
                # nearby tickets:
                entries = [int(x) for x in line.split(',')]
                for entry in entries:
                    valid = False
                    for valid_field in valid_fields:
                        for valid_range in valid_field["ranges"]:
                            if entry in valid_range:
                                valid = True

                    if not valid:
                        error_rate += entry
                pass
            else:
                pass
    return error_rate


def part2(input_data):
    """
    >>> part2(["class: 0-1 or 4-19","row: 0-5 or 8-19","seat: 0-13 or 16-19","","your ticket:","11,12,13","","nearby tickets:","3,9,18","15,1,5","5,14,9"])
    1
    """
    stage = 0
    valid_fields = []
    error_rate = 0
    own_ticket = []
    possible_fields = []
    for line in input_data:
        r_field_rule = regex_field_rule.match(line)
        if r_field_rule:
            # print(line)
            # print(r_field_rule.groups())
            valid_fields.append({
                "name": r_field_rule.group(1),
                "ranges": [
                    range(int(r_field_rule.group(2)), int(r_field_rule.group(3))+1),
                    range(int(r_field_rule.group(4)), int(r_field_rule.group(5))+1),
                ]
            })
            pass
        elif line.strip() == "your ticket:":
            stage = 1
        elif line.strip() == "nearby tickets:":
            stage = 2
        elif line.strip() == "":
            pass
        else:
            if stage == 1:
                # your ticket
                own_ticket = [int(x) for x in line.split(',')]
                possible_fields = [
                    [
                        field 
                        for field in valid_fields
                    ] 
                    for entry in own_ticket
                ]
                pass
            elif stage == 2:
                # nearby tickets:
                entries = [int(x) for x in line.split(',')]
                valid_line = True

                # check if valid
                for entry in entries:
                    valid_entry = False
                    for valid_field in valid_fields:
                        for valid_range in valid_field["ranges"]:
                            if entry in valid_range:
                                valid_entry = True
                    if not valid_entry:
                        valid_line = False

                if not valid_line:
                    continue

                # remove possible fields based on this entry
                for i, entry in enumerate(entries):
                    possible_fields[i] = [field for field in possible_fields[i] for r in field['ranges'] if entry in r]
                pass
            else:
                pass
    
    # while there is an entry with more than one possibility:
    while sum([len(x) == 1 for x in possible_fields]) != len(possible_fields):
        # select the first definite one
        for cur_field in possible_fields:
            if len(cur_field) == 1:
                # remove the field from all other options
                possible_fields = [
                    list(filter(lambda x: x != cur_field[0], fields)) 
                    if len(fields) != 1 else fields 
                    for fields in possible_fields
                ]

    product = 1
    for i, fields in enumerate(possible_fields):
        if fields[0]['name'].startswith("departure"):
            product *= own_ticket[i]
        pass
    return product


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass