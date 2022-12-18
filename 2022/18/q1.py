import numpy as np


def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    # load as grid
    positions = np.array([tuple(map(int, line.split(","))) for line in lines])
    # convert to zero based coords
    for dim in range(3):
        positions[:, dim] -= min(positions[:, dim])
    # Fill positions
    grid = np.zeros(shape=(np.max(positions[:, 0]) + 1, np.max(positions[:, 1]) + 1, np.max(positions[:, 2]) + 1))
    for pos in positions:
        grid[tuple(pos)] = 1

    sides = 0
    offsets = np.array([
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ])
    for pos in positions:
        for offset in offsets:
            pos2 = np.add(np.array(pos), offset)
            try:
                if (grid[tuple(pos2)] == 0) or np.any(pos2 == -1):
                    sides += 1
            except IndexError:
                sides += 1

    print(sides)
    return sides


if __name__ == '__main__':
    main(load_file(filename="in"))
