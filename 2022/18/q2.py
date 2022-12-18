import numpy as np

from utils import add_tuples


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    # load as grid
    positions = np.array([tuple(map(int, line.split(","))) for line in lines])
    # convert to zero based coords
    for dim in range(3):
        positions[:, dim] -= np.min(positions[:, dim])
    # Fill positions
    grid = np.zeros(shape=(np.max(positions[:, 0]) + 3, np.max(positions[:, 1]) + 3, np.max(positions[:, 2]) + 3))
    positions += 1
    for pos in positions:
        grid[tuple(pos)] = 1

    offsets = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]

    exposed = 0
    visited = set()
    q = [(0, 0, 0)]
    while q:
        p = q.pop(0)
        if p in visited:  # already visited
            continue

        visited.add(p)
        for offset in offsets:
            p2 = add_tuples(p, offset)
            if not (0 <= p2[0] < grid.shape[0] and 0 <= p2[1] < grid.shape[1] and 0 <= p2[2] < grid.shape[2]):
                continue
            if grid[tuple(p2)] == 1:  # inside a wall
                exposed += 1
                continue
            q.append(p2)

    for x in range(1, grid.shape[0] - 1):
        for y in range(1, grid.shape[1] - 1):
            for z in range(1, grid.shape[2] - 1):
                if (x, y, z) not in visited:
                    grid[(x, y, z)] = 1

    sides = 0
    for x in range(0, grid.shape[0]):
        for y in range(0, grid.shape[1]):
            for z in range(0, grid.shape[2]):
                for offset in offsets:
                    if grid[(x, y, z)] == 1 and grid[(add_tuples(offset, (x, y, z)))] == 0:
                        sides += 1

    print(sides)


if __name__ == '__main__':
    main(load_file(filename="in"))
