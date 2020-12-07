# Advent of Code 2020
# Day 07
# Author: irobin591

import os
import doctest
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

regex_entry = re.compile(r'^([a-z ]+) bags contain (.*)\.$')
regex_bag = re.compile(r'^([0-9]+) ([a-z ]*) bags?$')

class Bag():
    def __init__(self):
        self.color = ""
        self.direct_bags = {}
        pass

    def connect(self, bag_list):
        self.connected_bags = {
            bag_list[bag]: self.direct_bags[bag]
            for bag in self.direct_bags
        }

    @property
    def total_bags(self):
        bags = {}

        for bag in self.connected_bags:
            # print("  " + str(bag))
            total_bags = bag.total_bags
            multiplier = self.connected_bags[bag]
            for x in total_bags:
                if x not in bags:
                    bags[x] = 0
                bags[x] += multiplier * total_bags[x]
            if bag.color not in bags:
                bags[bag.color] = 0
            bags[bag.color] += multiplier
        return bags


def prep_input(input_data):
    bag_list = {}

    for entry_data in input_data:
        # x = entry.split('contain')
        # print(x)

        bag = Bag()

        entry = regex_entry.match(entry_data)
        if not entry:
            raise RuntimeError()
        # print(entry.groups())

        bag.color = entry.group(1)
        bag_list[bag.color] = bag
        # print(bag.color)

        content = entry.group(2).split(', ')
        # print(content)

        for single_content in content:
            r = regex_bag.match(single_content)
            if r:
                # print(r.groups())
                amount = int(r.group(1))
                bag_color = r.group(2)
                # print(bag)
                bag.direct_bags[bag_color] = amount

    for bag in bag_list:
        bag_list[bag].connect(bag_list)

    return bag_list


def test_bags():
    a = Bag()
    a.color = "a"

    b = Bag()
    b.color = "b"
    b.direct_bags["a"] = 3

    c = Bag()
    c.color = "c"
    c.direct_bags["a"] = 4
    c.direct_bags["b"] = 6

    bl = {
        "a": a,
        "b": b,
        "c": c
    }

    a.connect(bl)
    b.connect(bl)
    c.connect(bl)

    # print(a.total_bags)
    assert a.total_bags == {}
    # print(b.total_bags)
    assert b.total_bags == {'a': 3}
    # print(c.total_bags)
    assert c.total_bags == {'a': 22, 'b': 6}


def part1(input_data):
    """
    >>> part1(["light red bags contain 1 bright white bag, 2 muted yellow bags.","dark orange bags contain 3 bright white bags, 4 muted yellow bags.","bright white bags contain 1 shiny gold bag.","muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.","shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.","dark olive bags contain 3 faded blue bags, 4 dotted black bags.","vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.","faded blue bags contain no other bags.","dotted black bags contain no other bags."])
    4
    """
    bags = prep_input(input_data)

    return sum(["shiny gold" in bag.total_bags and bag.total_bags["shiny gold"] > 0 for bag in bags.values()])


def part2(input_data):
    """
    >>> part2(["light red bags contain 1 bright white bag, 2 muted yellow bags.","dark orange bags contain 3 bright white bags, 4 muted yellow bags.","bright white bags contain 1 shiny gold bag.","muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.","shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.","dark olive bags contain 3 faded blue bags, 4 dotted black bags.","vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.","faded blue bags contain no other bags.","dotted black bags contain no other bags."])
    32
    """
    bags = prep_input(input_data)

    return sum(bags["shiny gold"].total_bags.values())


if __name__ == "__main__":
    test_bags()
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass