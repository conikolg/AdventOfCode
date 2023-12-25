import re

import utils


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    lines: [tuple[str, int, str]] = [
        (direction, int(distance), color_code)
        for direction, distance, color_code in [
            re.findall(r"(\w) (\d+) \(#(\w{6})\)", line)[0]
            for line in lines
        ]
    ]

    # Compute all vertices
    vtx = [(0, 0)]  # x, y
    for direction, dist, _ in lines:
        if direction == "U":
            vtx.append(utils.add_tuples(vtx[-1], (0, dist)))
        elif direction == "D":
            vtx.append(utils.add_tuples(vtx[-1], (0, -dist)))
        elif direction == "L":
            vtx.append(utils.add_tuples(vtx[-1], (-dist, 0)))
        elif direction == "R":
            vtx.append(utils.add_tuples(vtx[-1], (dist, 0)))

    # simple bounding box
    botleft = (min(vert[0] for vert in vtx), min(vert[1] for vert in vtx))
    topright = (max(vert[0] for vert in vtx), max(vert[1] for vert in vtx))
    print(botleft, topright)

    # compute edges, always in a bottom-left to top-right direction
    edges = [
        vtx[i - 1] + vtx[i] if vtx[i - 1].__le__(vtx[i]) else vtx[i] + vtx[i - 1]
        for i in range(1, len(vtx))
    ]

    inside = 0
    for x in range(botleft[0], topright[0] + 1):
        for y in range(botleft[1], topright[1] + 1):
            if point_in_polygon((x, y), edges):
                inside += 1
    print(inside)


def point_in_polygon(point: tuple[int, int], edges: list[tuple]) -> bool:
    x, y = point
    intersections = 0

    # Shoot rays to the right
    for x1, y1, x2, y2 in edges:
        # Horizontal edges
        if y1 == y2:
            # On the edge
            if y == y1 and x1 <= x <= x2:
                return True
        # Vertical edges - inside if vertically between endpoints and to the left
        else:
            # Correct vertical location
            if y1 <= y < y2:
                # On the edge
                if x == x1:
                    return True
                # To the left of edge
                elif x < x1:
                    intersections += 1

    return intersections % 2 == 1


if __name__ == '__main__':
    main()
