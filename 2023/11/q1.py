def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    grid = [list(line) for line in lines]

    # expand rows
    for i in range(len(grid))[::-1]:
        if all(c == "." for c in grid[i]):
            grid.insert(i, list("." * len(grid[i])))
    # expand columns
    for j in range(len(grid[0]))[::-1]:
        if all(grid[i][j] == "." for i in range(len(grid))):
            for i in range(len(grid)):
                grid[i].insert(j, ".")

    galaxies: [tuple] = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == "#"
    ]

    answer = 0
    for i, g1 in enumerate(galaxies):
        for j, g2 in enumerate(galaxies):
            if j <= i:
                continue

            answer += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    print(answer)


if __name__ == '__main__':
    main()
