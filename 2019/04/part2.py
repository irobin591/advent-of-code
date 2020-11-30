import doctest
import re
import part1

# (0, 0) (1, 0)
# (0, 1) (1, 1)

def verify_p2(no: str) -> bool:
    """
    >>> verify_p2("112233")
    True
    >>> verify_p2("123444")
    False
    >>> verify_p2("111122")
    True
    """
    if not part1.verify_p1(no):
        return False

    double_duplicate = False

    counter = {}

    for c in no:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1

    for values in counter.values():
        if values == 2:
            return True

    return False

    
def part2(min_no: int, max_no: int) -> int:
    return len(list(part1.get_valid_codes(min_no, max_no, verify_p2)))


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        r = re.compile("^([0-9]*)-([0-9]*)$").match(infile.read())

        d = part2(int(r.group(1)), int(r.group(2)))

        print(d)
