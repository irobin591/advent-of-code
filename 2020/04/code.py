# Advent of Code 2020
# Day 04
# Author: irobin591

import os
import re
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n\n')

regex = re.compile(r'([a-z]{3}):(.*)')
regex_hgt = re.compile(r'^([0-9]{2,3})(cm|in)$')
regex_hcl = re.compile(r'^#([0-9a-f]{6})$')
regex_ecl = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
regex_pid = re.compile(r'^[0-9]{9}$')


class Passport():
    def __init__(self, data_string):
        da = data_string.replace('\n', ' ').split(' ')
        self.dict = dict([regex.match(x).groups() for x in da])
        pass

    def __str__(self):
        return str(self.dict)

    def __getitem__(self, key): 
        return self.dict[key]

    def is_valid(self):
        return ('byr' in self.dict and 
                'iyr' in self.dict and
                'eyr' in self.dict and
                'hgt' in self.dict and
                'hcl' in self.dict and
                'ecl' in self.dict and
                'pid' in self.dict) # and
                # cid in self.dict)

    def is_actual_valid(self):
        if not self.is_valid():
            return False
        
        if (int(self['byr']) < 1920 or int(self['byr']) > 2002 or
            int(self['iyr']) < 2010 or int(self['iyr']) > 2020 or
            int(self['eyr']) < 2020 or int(self['eyr']) > 2030):
            return False

        r_hgt = regex_hgt.match(self['hgt'])
        if not r_hgt:
            return False

        if r_hgt.group(2) == "cm":
            if int(r_hgt.group(1)) < 150 or int(r_hgt.group(1)) > 193:
                return False
        elif r_hgt.group(2) == "in":
            if int(r_hgt.group(1)) < 59 or int(r_hgt.group(1)) > 76:
                return False
        else:
            return False

        if not regex_hcl.match(self['hcl']):
            return False

        if not regex_ecl.match(self['ecl']):
            return False

        if not regex_pid.match(self['pid']):
            return False

        return True

def prep_data(input_data):
    return list(map(Passport, input_data))


def part1(input_data):
    """
    >> part1()
    None
    """
    data = prep_data(input_data)
    valid_passports = [passport for passport in data if passport.is_valid()]
    return len(valid_passports)


def part2(input_data):
    """
    >>> part2(["eyr:1972 cid:100\\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"])
    0
    >>> part2(["iyr:2019\\nhcl:#602927 eyr:1967 hgt:170cm\\necl:grn pid:012533040 byr:1946"])
    0
    >>> part2(["hcl:dab227 iyr:2012\\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"])
    0
    >>> part2(["hgt:59cm ecl:zzz\\neyr:2038 hcl:74454a iyr:2023\\npid:3556412378 byr:2007"])
    0
    >>> part2(["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\\nhcl:#623a2f"])
    1
    >>> part2(["eyr:2029 ecl:blu cid:129 byr:1989\\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"])
    1
    >>> part2(["hcl:#888785\\nhgt:164cm byr:2001 iyr:2015 cid:88\\npid:545766238 ecl:hzl\\neyr:2022"])
    1
    >>> part2(["iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"])
    1
    """
    data = prep_data(input_data)
    valid_passports = [passport for passport in data if passport.is_actual_valid()]

    import collections
    print(collections.Counter(list(map(lambda x: x['pid'], valid_passports))))
    return len(valid_passports)


if __name__ == "__main__":
    # doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass