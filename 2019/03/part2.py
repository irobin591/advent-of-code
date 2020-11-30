import part1
import doctest

DEBUG = False

def debug(msg):
    if DEBUG:
        print(msg)

def get_steps_to_intersection(path1, path2, intersection):
    debug(intersection)
    cur = []

    cur_pos1 = (0,0)
    cur_steps1 = 0
    for p1 in path1:
        if cur_pos1[0] != intersection[0] and cur_pos1[1] != intersection[1]:
            cur_pos1 = part1.move(cur_pos1, p1)
            cur_steps1 += int(p1[1:])
            continue

        debug("Pos1: {}".format(cur_pos1))

        direction1 = p1[0]
        steps1 = int(p1[1:])



        for _ in range(steps1):
            cur_pos1 = part1.move(cur_pos1, direction1 + "1")
            cur_steps1 += 1

            if cur_pos1 != intersection:
                continue
            debug("Pos1-Intersection: {}".format(cur_pos1))
            debug("Pos1-Steps: {}".format(cur_steps1))

            cur_pos2 = (0,0)
            cur_steps2 = 0

            for p2 in path2[:]:
                # print("{}".format(cur_pos2), end='')
                if cur_pos2[0] != intersection[0] and cur_pos2[1] != intersection[1]:
                    cur_pos2 = part1.move(cur_pos2, p2)
                    cur_steps2 += int(p2[1:])
                    continue

                debug("Pos2: {}".format(cur_pos2))


                direction2 = p2[0]
                steps2 = int(p2[1:])

                for _ in range(steps2):
                    cur_pos2 = part1.move(cur_pos2, direction2 + "1")
                    cur_steps2 += 1

                    if cur_pos2 != intersection:
                        continue
                    debug("Pos2-Intersection: {}".format(cur_pos2))
                    debug("Pos2-Steps: {}".format(cur_steps2))


                    cur.append(cur_steps1 + cur_steps2)

    # print()
    return min(cur) if len(cur) > 0 else 99999999



    
def part2(path1, path2):
    """
    >>> part2("R8,U5,L5,D3", "U7,R6,D4,L4")
    30
    >>> part2("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")
    610
    >>> part2("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    410
    """

    p1 = path1.split(',')
    p2 = path2.split(',')

    intersections =  part1.get_intersections(p1, p2)[1:]

    steps_to_intersection = [get_steps_to_intersection(p1, p2, i) for i in intersections]

    dist = min(steps_to_intersection)

    return dist


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        paths = list(map(lambda x: x.strip(), infile))

        d = part2(paths[0], paths[1])

        print(d)
