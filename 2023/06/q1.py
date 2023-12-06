import operator
from functools import reduce

import utils


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    times: [int] = utils.int_split(lines.pop(0).split(":")[1])
    dists: [int] = utils.int_split(lines.pop(0).split(":")[1])
    ways: [int] = []

    for i in range(len(times)):
        ways.append(0)
        for t in range(1, times[i]):
            dist = (times[i] - t) * t
            if dist > dists[i]:
                ways[-1] += 1

    print(ways)
    print(reduce(operator.mul, ways, 1))


if __name__ == '__main__':
    main()
