def main():
    with open("in.txt", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    grid = [list(line) for line in lines]
    expansion = 1_000_000

    rows: [int] = [
        i
        for i, line in enumerate(grid)
        if all(c == "." for c in line)
    ]

    cols: [int] = [
        j
        for j in range(len(grid[0]))[::-1]
        if all(grid[i][j] == "." for i in range(len(grid)))
    ]

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

            r1, r2 = min(g1[0], g2[0]), max(g1[0], g2[0])
            c1, c2 = min(g1[1], g2[1]), max(g1[1], g2[1])
            erows = len([r for r in rows if r1 < r < r2])
            ecols = len([c for c in cols if c1 < c < c2])
            answer += r2 - r1 + erows * (expansion - 1)
            answer += c2 - c1 + ecols * (expansion - 1)

    print(answer)


if __name__ == '__main__':
    main()
