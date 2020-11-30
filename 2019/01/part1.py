from math import floor
import doctest

def calc_fuel(mass):
    """
    >>> calc_fuel(12)
    2
    >>> calc_fuel(14)
    2
    >>> calc_fuel(1969)
    654
    >>> calc_fuel(100756)
    33583
    """
    return (mass//3)-2


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        fuel_sum = sum(map(lambda l: calc_fuel(int(l)), infile))
        print("sum: {}".format(fuel_sum))
