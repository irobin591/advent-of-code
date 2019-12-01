import doctest
from part1 import *

def calc_fuel_recursive(mass):
    """
    Calc fuel for current mass and recursive fuel needed for that fuel

    >>> calc_fuel_recursive(14)
    2
    >>> calc_fuel_recursive(1969)
    966
    >>> calc_fuel_recursive(100756)
    50346
    """

    fuel = calc_fuel(mass)
    if fuel <= 0:
        return 0

    return fuel + calc_fuel_recursive(fuel)


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        fuel_sum = sum(map(lambda l: calc_fuel_recursive(int(l)), infile))
        print("sum: {}".format(fuel_sum))

