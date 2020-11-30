from math import floor
import doctest

# (0, 0) (1, 0)
# (0, 1) (1, 1)

def move(cur_pos, instruction):
    """
    >>> move((0, 0), "R42")
    (42, 0)
    >>> move((0, 0), "L42")
    (-42, 0)
    >>> move((0, 0), "U42")
    (0, -42)
    >>> move((0, 0), "D42")
    (0, 42)
    """
    direction = instruction[0]
    length = int(instruction[1:])

    next_pos = cur_pos

    if direction == "R":
        next_pos = (cur_pos[0] + length, cur_pos[1])
    if direction == "L":
        next_pos = (cur_pos[0] - length, cur_pos[1])
    if direction == "U":
        next_pos = (cur_pos[0], cur_pos[1] - length)
    if direction == "D":
        next_pos = (cur_pos[0], cur_pos[1] + length)

    return next_pos


def get_points(start, path):
    points = [start]
    for instruction in path:
        points.append(move(points[-1], instruction))
    return points

def get_intersections(path1, path2):
    points_p1 = get_points((0, 0), path1)
    points_p2 = get_points((0, 0), path2)

    intersections = []

    for pp1 in range(len(points_p1)-1):
        for pp2 in range(len(points_p2)-1):
            pp1a = points_p1[pp1]
            pp1b = points_p1[pp1+1]

            pp2a = points_p2[pp2]
            pp2b = points_p2[pp2+1]

            # p1x = (min(pp1a[0], pp1b[0]), max(pp1a[0], pp1b[0]))
            # p1y = (min(pp1a[1], pp1b[1]), max(pp1a[1], pp1b[1]))
            # p2x = (min(pp2a[0], pp2b[0]), max(pp2a[0], pp2b[0]))
            # p2y = (min(pp2a[1], pp2b[1]), max(pp2a[1], pp2b[1]))
            p1x = (min(pp1a[0], pp1b[0]), max(pp1a[0], pp1b[0]))
            p1y = (min(pp1a[1], pp1b[1]), max(pp1a[1], pp1b[1]))
            p2x = (min(pp2a[0], pp2b[0]), max(pp2a[0], pp2b[0]))
            p2y = (min(pp2a[1], pp2b[1]), max(pp2a[1], pp2b[1]))

            p1_horizontal = p1x[0] == p1x[1]
            p2_horizontal = p2x[0] == p2x[1]
            
            # One line is horizonal and the other is vertical
            if (p1_horizontal and not p2_horizontal) or (not p1_horizontal and p2_horizontal):
                # Intersection on x axis
                if p1x[0] <= p2x[1] and p1x[1] >= p2x[0]:
                    if p1y[0] <= p2y[1] and p1y[1] >= p2y[0]:
                        if p1_horizontal:
                            x = p1x[0]
                            y = p2y[0]
                            intersections.append((x, y))
                        if p2_horizontal:
                            x = p2x[0]
                            y = p1y[0]
                            intersections.append((x, y))

            # Both lines are horizontal
            if p1_horizontal and p2_horizontal:
                # Check if lines are on the same height
                if p1x[0] == p2x[0]:
                    x = p1x[0]
                    # Check if they intersect
                    if p1y[0] <= p2y[1] and p1y[1] >= p2y[0]:
                        l = max(p1y[0], p2y[0])
                        r = min(p1y[1], p2y[1]) 
                        for y in range(r-l+1):
                            intersections.append((x, l+y))
                            
            # Both lines are vertical
            if not p1_horizontal and not p2_horizontal:
                # Check if lines are on the same height
                if p1y[0] == p2y[0]:
                    y = p1y[0]
                    # Check if they intersect
                    if p1x[0] <= p2x[1] and p1x[1] >= p2x[0]:
                        l = max(p1x[0], p2x[0])
                        r = min(p1x[1], p2x[1]) 
                        for x in range(r-l+1):
                            intersections.append((l+x, y))


            # if pp1a[0] == pp1b[0] and pp2a[1] == pp2b[1]:
            #     if pp1a[1] <= pp2a[1] and pp1b[1] >= pp2a[1] and
            #         pp2a[0] <= pp1a[0] and pp2b[0] >= pp1a[0]:
            #         intersections.append((pp1a[0], pp1b[1]))
            #     pass
            # if pp1a[1] == pp1b[1] and pp2a[0] == pp2b[0]:
            #     pass
            # if pp1a[0] == pp1b[0] and pp2a[0] == pp2b[0]:
            #     pass
            # if pp1a[1] == pp1b[1] and pp2a[1] == pp2b[1]:
            #     pass

    return intersections

def dist_to_closest_intersection(path1, path2):
    intersections = get_intersections(path1, path2)

    def get_dist(point):
        return abs(point[0]) + abs(point[1])

    dists = sorted(list(map(get_dist, intersections)))

    # print(dists)

    return dists[1]

    
def part1(path1, path2):
    """
    >>> part1("R8,U5,L5,D3", "U7,R6,D4,L4")
    6
    >>> part1("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83")
    159
    >>> part1("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    135
    """

    p1 = path1.split(',')
    p2 = path2.split(',')

    return dist_to_closest_intersection(p1, p2)


if __name__ == "__main__":
    doctest.testmod()

    with open('input.txt', 'r') as infile:
        paths = list(map(lambda x: x.strip(), infile))

        d = part1(paths[0], paths[1])

        print(d)
