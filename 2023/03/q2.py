from collections import defaultdict

import utils


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    symbols = [
        (i, j)
        for i in range(len(lines))
        for j in range(len(lines[i]))
        if lines[i][j] == "*"
    ]

    # check positions around
    gears = defaultdict(set)
    for i, j in symbols:
        for (i2, j2), val in utils.get_grid_neighbors(lines, (i, j), True, True, True, True, True):
            if val in "1234567890":
                while j2 > 0 and lines[i2][j2 - 1] in "1234567890":
                    j2 -= 1
                gears[(i, j)].add((i2, j2))

    answer = 0
    for num_locs in gears.values():
        if len(num_locs) != 2:
            continue

        p1, p2 = list(num_locs)
        r1 = ""
        i, j = p1
        while j < len(lines[i]) and lines[i][j] in "1234567890":
            r1 += lines[i][j]
            j += 1

        r2 = ""
        i, j = p2
        while j < len(lines[i]) and lines[i][j] in "1234567890":
            r2 += lines[i][j]
            j += 1

        answer += int(r1) * int(r2)

    print(answer)


if __name__ == '__main__':
    main()
