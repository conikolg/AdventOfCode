import utils


def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    symbols = [
        (i, j)
        for i in range(len(lines))
        for j in range(len(lines[i]))
        if lines[i][j] not in "1234567890."
    ]

    # check positions around
    part_locations = set()
    for i, j in symbols:
        for (i2, j2), val in utils.get_grid_neighbors(lines, (i, j), True, True, True, True, True):
            if val in "1234567890":
                while j2 > 0 and lines[i2][j2 - 1] in "1234567890":
                    j2 -= 1
                part_locations.add((i2, j2))

    answer = 0
    for (i, j) in part_locations:
        num = ""
        while j < len(lines[i]) and lines[i][j] in "1234567890":
            num += lines[i][j]
            j += 1
        answer += int(num)

    print(answer)


if __name__ == '__main__':
    main()
