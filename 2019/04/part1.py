import doctest
import re

# (0, 0) (1, 0)
# (0, 1) (1, 1)

def verify_p1(no: str) -> bool:
    """
    >>> verify_p1("111111")
    True
    >>> verify_p1("223450")
    False
    >>> verify_p1("123789")
    False
    """
    if len(no) != 6:
        return False
    
    duplicate = False

    last_digit = no[0]
    to_check = no[1:]
    while len(to_check) != 0:
        digit = to_check[0]

        if digit == last_digit:
            duplicate = True
        
        try:
            if int(digit) < int(last_digit):
                return False
        except:
            return False

        last_digit = digit
        to_check = to_check[1:]

    if not duplicate:
        return False

    return True

def get_valid_codes(min_no: int, max_no: int, verify):
    for x in range(min_no, max_no+1):
        if verify(str(x)):
            yield x
    
def part1(min_no: int, max_no: int) -> int:
    return len(list(get_valid_codes(min_no, max_no, verify_p1)))


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        r = re.compile("^([0-9]*)-([0-9]*)$").match(infile.read())

        d = part1(int(r.group(1)), int(r.group(2)))

        print(d)
