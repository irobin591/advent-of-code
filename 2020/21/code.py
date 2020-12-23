# Advent of Code 2020
# Day 21
# Author: irobin591

import os
import doctest
import re

re_entry = re.compile(r'^([a-z ]+) \(contains ([a-z, ]*)\)$')

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n')


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    5
    """

    # dict['allergen'] = ['asdfa', 'agbsfb']
    allergens = {}
    ingredients = []

    # map strings to allergens
    for entry in input_data:
        r = re_entry.match(entry)

        if not r:
            raise RuntimeError("")

        contents = set(r.group(1).split(' '))
        ingredients.extend(contents)
        for allergen in r.group(2).split(', '):
            if allergen not in allergens:
                allergens[allergen] = contents
            else:
                # only keep already added ingredients
                allergens[allergen] = [ingredient for ingredient in contents if ingredient in allergens[allergen]]

    # print(allergens)
    # print(ingredients)

    ingredients_with_allergens = set([y for x in allergens.values() for y in x])
    # print(list(filter(lambda i: i not in ingredients_with_allergens, ingredients)))

    return len(list(filter(lambda i: i not in ingredients_with_allergens, ingredients)))


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n'))
    'mxmxvkd,sqjhc,fvjkl'
    """
    # dict['allergen'] = ['asdfa', 'agbsfb']
    allergens = {}
    ingredients = []
    
    # map strings to allergens
    for entry in input_data:
        r = re_entry.match(entry)

        if not r:
            raise RuntimeError("")

        contents = set(r.group(1).split(' '))
        ingredients.extend(contents)
        for allergen in r.group(2).split(', '):
            if allergen not in allergens:
                allergens[allergen] = list(contents)
            else:
                # only keep already added ingredients
                allergens[allergen] = [ingredient for ingredient in contents if ingredient in allergens[allergen]]

    # print(allergens)

    # (allergen, ingredient)
    assigned_allergens = []

    while sum([len(ingreds) for ingreds in allergens.values()]) > 0:
        for allergen in allergens:
            if len(allergens[allergen]) == 1:
                ingredient = allergens[allergen][0]
                assigned_allergens.append((allergen, ingredient))
                for allergen2 in allergens:
                    if ingredient in allergens[allergen2]:
                        allergens[allergen2].remove(ingredient)

    assigned_allergens.sort(key=lambda x: x[0])

    return ",".join([x[1] for x in assigned_allergens])


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass